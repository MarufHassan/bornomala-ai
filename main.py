#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:05:01 2019

@author: rownak
"""

from __future__ import print_function
from flask import Flask, render_template
from flask import request, jsonify
from keras import backend as K

from keras.models import load_model

import os
import numpy as np
import cv2
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("templates/static/")

@app.route('/', methods=['GET'])
def index():
    title = 'স্বরবর্ণ'
    return render_template('layouts/landing_page.html', title=title)

@app.route('/canvas', methods=['GET'])
def show():
    title = 'স্বরবর্ণ'
    return render_template('layouts/index.html', title=title)

def segment(image):
	rows = image.shape[0]
	cols = image.shape[1]

	trow, drow, lcol, rcol = cols + 1, -1, rows + 1, -1

	# left most column
	for r in range(0, rows):
		for c in range(0, cols):
			if image[r][c] != 255 and c < lcol:
				lcol = c
				break

	# right most column
	for r in range(rows - 1,  -1, -1):
		for c in range(cols):
			if image[r][c] != 255 and c > rcol:
				rcol = c
				break

	# left most row
	for c in range(cols):
		for r in range(rows):
			if image[r][c] != 255 and r < trow:
				trow = r
				break

	# right most row
	for c in range(cols - 1, -1, -1):
		for r in range(rows - 1, -1, -1):
			if image[r][c] != 255 and r > drow:
				drow = r
				break

	if trow == cols + 1 or drow == -1 or lcol == rows + 1 or rcol == -1:
		return image
	print(trow, drow, lcol, rcol)
	return image[trow:drow,lcol:rcol]

@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    alphabets = ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']
    data_url = request.form['canvas_data']
    offset = data_url.index(',')+1
    img_bytes = base64.b64decode(data_url[offset:])
    img = Image.open(BytesIO(img_bytes))
    img  = np.array(img)
    cv2.imwrite('picture.png',img)
      
    classifier = load_model('model.h5')
    img = cv2.imread("picture.png", cv2.IMREAD_GRAYSCALE)
    im = segment(img)
    # cv2.imwrite('trial2.png',im)
    im_resized = cv2.resize(im, (32, 32))
    im = im_resized.reshape(32, 32, 1)
    im = im.reshape(1, 32, 32, 1)
    result = classifier.predict(np.array(im))
    a = np.argmax(result)
    K.clear_session()
    params = { "char" : alphabets[a] }
    return jsonify(params)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)