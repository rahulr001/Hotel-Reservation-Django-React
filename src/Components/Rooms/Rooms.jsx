import React,{useState} from 'react';
import './Rooms.css';
import {Link} from 'react-router-dom';
import {FaWifi,FaTv,FaDoorClosed} from 'react-icons/fa';



function Rooms({rooms ,fromdate,todate}) {
  
  
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  

  return (
    <div className='main-container'>
      <div className='room-container'>
      <div className='g-left'>
       <img src={rooms.imageurls[0]} alt=''/> 
      
      </div>
      <div className="g-right">
       <h1>Name: {rooms.name}</h1>
       <h6>Type: {rooms.type}</h6> 
       <h6>Max-Count: {rooms.maxcount}</h6>
       <h6>{<div className='room-icons'><FaWifi/>&emsp;<FaTv/>&emsp;<FaDoorClosed/></div>}</h6>
       <Link to={`/viewdetails/${rooms._id}/${fromdate}/${todate}`}>
       <button className="btn btn-primary button-room" onClick={handleShow}>View-Details</button>
       </Link>
       <Link to={`/book/${rooms._id}/${fromdate}/${todate}`}>
       <button disabled={!fromdate && !todate} className="btn btn-success book-btn">Book-Now</button>
       </Link>
       </div>
      </div>
     </div>
    )
}

export default Rooms