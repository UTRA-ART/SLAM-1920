import React from 'react';
import p5 from 'p5';

export class Whiteboard extends React.Component {

  constructor(props) {
    super(props);

    this.position = {
      position: "absolute",
      top: this.props.top,
      left: this.props.left
    }
  }

  componentDidMount() {
    this.canvas = new p5(this.props.sketch, this.wrapper);
    if( this.canvas.myCustomRedrawAccordingToNewPropsHandler ) {
      this.canvas.myCustomRedrawAccordingToNewPropsHandler(this.props);
    }
  }

  componentWillReceiveProps(newprops) {
    if(this.props.sketch !== newprops.sketch){
      this.wrapper.removeChild(this.wrapper.childNodes[0]);
      this.canvas = new p5(newprops.sketch, this.wrapper);
    }
    if( this.canvas.myCustomRedrawAccordingToNewPropsHandler ) {
      this.canvas.myCustomRedrawAccordingToNewPropsHandler(newprops);
    }
  }

  render() {
    return <div style = {this.position} ref={wrapper => this.wrapper = wrapper}></div>;
  }
}