import { Wave } from './objs/Wave'

export function player (canvas) {

  var wave;

  canvas.setup = function () {
    canvas.createCanvas(canvas.windowWidth, 100);

    wave = new Wave(this.width, this.height);
  };

  
  canvas.myCustomRedrawAccordingToNewPropsHandler = function (props) {
  };


  canvas.draw = function () {
    
      canvas.clear();
      canvas.stroke(255);

      wave.update();
      wave.draw(canvas);
  };

};
