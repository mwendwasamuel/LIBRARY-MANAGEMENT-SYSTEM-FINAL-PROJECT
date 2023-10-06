import React, { Component } from 'react';
import Clock from 'react-live-clock'; // Import the Clock component
import '../Front/Css/Footer.css';

class Footer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            date: '',
        };
    }

    componentDidMount() {
        console.log(new Date().getDate());
    }

    render() {
        return (
            <div>
                <div className="foot">
                    <h2 className="date">© Online Library Management System, {new Date().toDateString()}</h2>
                    {/* Use the Clock component */}
                    <Clock format={'HH:mm:ss'} ticking={true} timezone={'US/Pacific'} />
                </div>
            </div>
        );
    }
}

export default Footer;
