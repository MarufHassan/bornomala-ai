$( document ).ready(function() {
  $("#loading").hide();
  function createCanvas(parent, width, height) {
    var canvas = document.getElementById("inputCanvas");
    canvas.context = canvas.getContext('2d');
    return canvas;
  }

  function init(container, width, height, fillColor) {

    var canvas = createCanvas(container, width, height);
    var ctx = canvas.context;
    ctx.fillCircle = function(x, y, radius, fillColor) {
      this.fillStyle = fillColor;
      this.beginPath();
      this.moveTo(x, y);
      this.arc(x, y, radius, 0, Math.PI * 2, false);
      this.fill();
    };
    ctx.clearTo = function(fillColor) {
      ctx.fillStyle = fillColor;
      ctx.fillRect(0, 0, width, height);
    };
    ctx.clearTo("#fff");

    canvas.onmousemove = function(e) {
      if (!canvas.isDrawing) {
        return;
      }
      var x = e.pageX - this.offsetLeft;
      var y = e.pageY - this.offsetTop;
      var radius = 10;
      var fillColor = 'rgb(0,0,0)';
      ctx.fillCircle(x, y, radius, fillColor);
    };
    canvas.onmousedown = function(e) {
      canvas.isDrawing = true;
    };
    canvas.onmouseup = function(e) {
      canvas.isDrawing = false;
    };
    canvas.mouseleave = function(e) {
      canvas.isDrawing = false;
    };
  }

  var container = document.getElementById('canvas');
  init(container, 1000, 400, '#34eb95');

  function clearCanvas() {
    var canvas = document.getElementById("inputCanvas");
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0,0,canvas.width, canvas.height);
    canvas.isDrawing = false;
  }

  function getData() {
    var canvas = document.getElementById("inputCanvas");
    var imageData = canvas.context.getImageData(0, 0, canvas.width, canvas.height);
      $("#loading").show();
      $.post( "/postmethod", {
      canvas_data: JSON.stringify(canvas.toDataURL())
      
    }, function(data, req, resp){
         //alert(Object.values(data));  \
         $("#loading").hide();
         var popup = document.getElementById('myModal');
         var span = document.getElementsByClassName("end")[0];
         popup.style.display = "block";
         document.getElementById("display_content").textContent=Object.values(data);
            
         span.onclick = function() {
            popup.style.display = "none";
         }    
    }); 
  }

  $( "#clearButton" ).click(function(){
    clearCanvas();
  });

  $( "#sendButton" ).click(function(){
    getData();
  });
});