import React, { Component } from 'react'
import  '../Front/Css/Footer.css'
import Clock from 'react-live-clock';


export default class About extends Component {
    render() {
        return (
            <div>

        <h1>Scenario Of Project</h1>
                <div  class="row">
                    <div className="col-sm-1"></div>
					<div className="col-sm-10 csshobe">
				   <p > <b className="fontsize">
                   The Library Management System is a Library Management website for monitoring and controlling the transactions in a library. There has high authentication system. Authentication has a username & password for login. Only staff can log in. The staff has a name, id. The staff maintains books from the library. A book has Author, SR no which is unique, publisher, price, category, title, ISBN. The staff also keeps track of readers.  A reader has a unique id, first name, last name,  department, phone no.  Readers issue books from library and books reserve date reserve under readers id. Readers have to return books within return dates.
                   </b> </p>
				 </div>
				 </div>


               <div className="row footer">
                   <div className="col-sm-4">
                    <h2 className="deve"> <u>Developer</u> </h2>
                    <h6>Samuel Mbula </h6> 
                    <h6>Elijah Njora</h6>
                   </div>
                   <div className="col-sm-4">

                   {/* <dib className="row">
                       <h2 className="clock col-sm-4">  <Clock   format={'HH:mm:ss'} ticking={true} timezone={'UTC +6'} /></h2>
           <h2 className="date">{  new Date().toDateString() }</h2>
           </dib> */}
                   </div>
                   <div className="col-sm-4">
                   <h2 className="deve"> <u>Contact Us</u> </h2>
                   <h6>Samuel Mbula</h6>
                   <h6>Elijah </h6>
                  <p className="deve"> <a  href="https://www.facebook.com/Asherleeky?mibextid=ZbWKwL"> <i class="fab fa-facebook-square"></i> </a> </p>
                  <p className="deve"> <a  href="https://twitter.com/LeekyAsher"> <i class="fab fa-twitter-square"></i> </a> </p>
                   </div>
                   </div>
            </div>
        )
    }
}
