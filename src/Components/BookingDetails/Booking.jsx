import React from 'react';
import './Booking.css';


function Booking({room}) {
    
   
  return (
    <div className='booking-container'>
        <div className='booksub-container'>
            
            <div className='b-right'>
             <div className="user-details">
                <h1>hello bro</h1>
             </div>
            </div>
            <div className="b-left">
                <div className="book-content">
                <div className="room-details">
                    <h1>{room.name}</h1>
                    <p>Max-Count: {room.maxcount}</p>
                    <p>Type: {room.type}</p>
                </div>
                <div className="room-img">
                <img src={room.imageurls[0]} alt="" />
                </div>
                </div>
                <div className="amount">
                    <h1>Amount</h1>
                    <p>Total-Day:</p>
                    <p>Rent-per-day:</p>
                    <p>Total-Amount:</p>
                    </div>
               
          </div>
        </div>
     </div>
  )
}

export default Booking