import React from 'react';


export class Button extends React.Component {
    constructor(props) {
        super(props);

        this.pos = {
            position: "absolute",
            top: this.props.top,
            left: this.props.left
        };
    }

    render() {
        return (
        <div style = {this.pos} > 
            <button className = {this.props.styles}>{ this.props.text }</button>
        </div>
        );
    }
}