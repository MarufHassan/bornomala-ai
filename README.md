# Bornomala

An experimental app for web that performs real-time bangla vowel handwritten character recognition captured using web canvas.

## Project Demo Video

[![Watch the video](https://img.youtube.com/vi/YPs3-d9UG-8/0.jpg)](https://youtu.be/YPs3-d9UG-8)

## Technologies

* Deep Learning

     - Convolution Neural Network (CNN)
     - Python, keras, tensorflow, opencv, numpy

* Web

     - Flask (python web framework)
     - Jquery, Ajax, Bootstrap

## Dataset

A data file is required for every language you want to recognize. The dataset was obtained online from the [CMATERdb](https://www.dropbox.com/s/55bhfr3ycvsewsi/CMATERdb%203.1.2.rar) pattern recognition database repository. It consists of a Train folder and a Test folder, containing 12,000 and 3,000 images respectively. We only used vowels in our work.

- For training data, we found 2112 images belonging to 11 classes.
- For test data, we found 528 images belonging to 11 classes.

## CNN Model Summary

     _________________________________________________________________
     Layer (type)                 Output Shape              Param #   
     =================================================================
     conv2d_1 (Conv2D)            (None, 30, 30, 32)        320       
     _________________________________________________________________
     max_pooling2d_1 (MaxPooling2 (None, 15, 15, 32)        0         
     _________________________________________________________________
     conv2d_2 (Conv2D)            (None, 13, 13, 64)        18496     
     _________________________________________________________________
     batch_normalization_1 (Batch (None, 13, 13, 64)        256       
     _________________________________________________________________
     max_pooling2d_2 (MaxPooling2 (None, 6, 6, 64)          0         
     _________________________________________________________________
     dropout_1 (Dropout)          (None, 6, 6, 64)          0         
     _________________________________________________________________
     conv2d_3 (Conv2D)            (None, 4, 4, 128)         73856     
     _________________________________________________________________
     batch_normalization_2 (Batch (None, 4, 4, 128)         512       
     _________________________________________________________________
     max_pooling2d_3 (MaxPooling2 (None, 2, 2, 128)         0         
     _________________________________________________________________
     dropout_2 (Dropout)          (None, 2, 2, 128)         0         
     _________________________________________________________________
     flatten_1 (Flatten)          (None, 512)               0         
     _________________________________________________________________
     dense_1 (Dense)              (None, 256)               131328    
     _________________________________________________________________
     dense_2 (Dense)              (None, 512)               131584    
     _________________________________________________________________
     dense_3 (Dense)              (None, 100)               51300     
     _________________________________________________________________
     dense_4 (Dense)              (None, 11)                1111      
     =================================================================
     Total params: 408,763
     Trainable params: 408,379
     Non-trainable params: 384
     _________________________________________________________________

## Installation

To build and run the app, first of all clone this project.

You may also consider installing the following **dependencies**:

- [TensorFlow](https://www.tensorflow.org/install/).
- [Keras](https://keras.io/#installation).
- [Open CV](https://pypi.org/project/opencv-python/).
- [Flask](https://pypi.org/project/Flask/).

Then open `cmd` in the project directory and run the command `python main.py`.