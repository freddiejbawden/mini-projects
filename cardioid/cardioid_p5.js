var total = 400;
var multiple = 1;
var text_buffer = 100;
let mod_slider, total_slider;

function setup() {
  createCanvas(500 + text_buffer,500 + text_buffer);
  frameRate(30)
  textFont("Arial");
  mod_slider = createSlider(0, 1000, 2);
  mod_slider.position(10, 500+60);
  mod_slider.style('width', '500px')
  mod_slider.style('color', 'white')
}

function draw() {
  const multiple = mod_slider.value()/100
  background(0);
  var r = (width-text_buffer)/2;
  translate((width)/2, (height-text_buffer)/2 + 10);
  stroke(255);
  noFill();
  circle(0,0,r*2);
  
  for (var i = 0; i < total; i++) {
     var pos = convertNumToPos(i, r);
     fill(255);
     var mod_val = (int)(i*multiple % total);
     var link = convertNumToPos((int)(i*multiple % total),r);
     stroke(255-map(mod_val, 0,total, 0, 255),0,map(mod_val, 0,total, 0, 255));
     line(pos[0],pos[1],link[0],link[1]);
  }
   
  text("Mod: " + multiple.toFixed(2), -250, 250);
}


function convertNumToPos(num, r) {
   var angle = map(num,0, total, 0, TWO_PI);
   var x = r * cos(angle);
   var y = r * sin(angle);
   return [x,y];
}
