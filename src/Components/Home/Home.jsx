import React from 'react';
import './Home.css';
import {Link} from 'react-router-dom'
import BG from '../Assets/bg1.jpg'

function Home() {
  return (
    <div className='home-container'>
     <div className='home-top'>
      <img src='https://wallpapershome.com/images/pages/pic_h/560.jpg' alt="" />
      </div>
      <div className="home-cards">
        <div className="card-1">
          <img src="https://wallpapershome.com/images/pages/pic_h/19257.jpg" alt="" />
          <h1>To Book Rooms</h1>
          <p>We had a Exoitic Rooms to make your stay most memorable and enjoyable
            click a button soon to Book your Rooms</p>
            <Link to='/roompage'>
            <button className='btn btn-success hbtn'>Book-Now</button>
            </Link>
            
        </div>
        <div className="card-2">
        <img src="https://wallpapershome.com/images/pages/pic_h/19257.jpg" alt="" />
        <h1>To Party-Hall</h1>
          <p>We had a Exoitic Hall to make your events most memorable and enjoyable
            click a button soon to Book your Hall</p>
            <button className='btn btn-success hbtn'>Book-Now</button>
        </div>
      </div>
    </div>
  )
}

export default Home;