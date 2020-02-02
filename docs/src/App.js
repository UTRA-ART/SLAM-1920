import React, { Component } from 'react';

//css imports
import './App.css';
import './components/button/buttons.css'


//react components
//eslint-disable-next-line
import { Button } from './components/button/Button.js'


//p5 canvas wrapper
import { Whiteboard } from './Whiteboard';

//sketches
import { player } from './player/player';
import { scope } from './scope/Scope'


class App extends Component {
  render() {
    return (
      <div className = "background">
        <Whiteboard top = {0} left = {0} sketch = { scope } />
        <Whiteboard top = {0} left = {0} sketch = { player } />
      </div>
    );
  }
}

export default App;
