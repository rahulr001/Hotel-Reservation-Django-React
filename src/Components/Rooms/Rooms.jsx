import React,{useState} from 'react';
import './Rooms.css';
import {Modal,Carousel} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import BookingPage from '../../Pages/Booking-Page';


function Rooms({rooms}) {
  
  
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
       <h1>Name:{rooms.name}</h1>
       <h6>Max-Count:{rooms.maxcount}</h6>
       <h6>Type:{rooms.type}</h6>
       <button className="btn button-room" onClick={handleShow}>View-Details</button>
       <Link to={`/book/${rooms._id}`}>
       <button className="btn book-btn">Book-Now</button>
       </Link>
       </div>
       <div>  
      <Modal show={show} onHide={handleClose} size='lg'>
        <Modal.Header>
          <Modal.Title>{rooms.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <Carousel>
        {
              rooms.imageurls.map(url=>{
                return<Carousel.Item>
                   <img className='carosel-img' src={url} alt="" />
                   </Carousel.Item>
              })
          }
        
        </Carousel>
        <p><strong>Room-Description :</strong>{rooms.description}</p>
        </Modal.Body>
        <Modal.Footer>
          <div>
          <button className='btn close-btn' onClick={handleClose}>
            Close
          </button>
          </div>
        </Modal.Footer>
      </Modal>
      </div>
      </div>
     </div>
    )
}

export default Rooms