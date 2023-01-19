import React,{useEffect,useState} from 'react';
import { Tabs } from 'antd';
import 'antd/dist/reset.css';
import './Profile.css';
import {  useNavigate } from "react-router-dom";
import Loading from '../Loading/Loading';
import axios from 'axios';
import moment from 'moment';
const {TabPane}=Tabs;

function Profile() {
  const user = JSON.parse(localStorage.getItem("currentUser"))
  let navigate = useNavigate();
  useEffect(()=>{
    if(!user){
      let path = `/login`; 
      navigate(path);
    }
  },[])
    
    
  return (
    <div className='profile-container'>
      <img src="https://wallpapershome.com/images/pages/pic_h/11163.jpg" alt=""/>
      <div className="profile-bg">
        
      </div>
    <div className="tab-con">

      <Tabs className='tabs-header' defaultActiveKey='1'>
      {/* <TabPane tab="Profile" key='1'>
        <div className="profile-tab">
        <h1>My-Profile</h1>
          <h3>Name : {user.username}</h3>
          <h3>Email:{}</h3>
        </div>
        </TabPane> */}
        <TabPane tab="My-Bookings" key='2'>
        <div className="profile-tab">
        <Mybookings/>
        </div>
        </TabPane>
        </Tabs>
        </div>
    </div>
  )
}

export default Profile;



export function Mybookings() {
  
  const user = JSON.parse(localStorage.getItem("currentUser"));
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState();
  const [bookings,setBookings]=useState([]);

  
  async function getdata(){
    try{
      setLoading(true)
       await axios.get("http://rahulr0001.pythonanywhere.com/hotel/roomBookingDetails/",{userid:'user_id'})
      .then(res=>{console.log(res.data)
        setBookings(res.data)})
      setLoading(false)
      
    }catch(error){
      setError(error)
      console.log(error);
    }
  }
useEffect(()=>{
 getdata()
},[])

// function cancelBooking(bookingid,roomid){
//     setLoading(true)

// }
  return (
    <div className='mybook-container'>
      <div className="loading" style={{zIndex:'-1'}}>
      {loading && (<Loading/>)}
      </div>
      {bookings && (bookings.map(book=>{
        return <div className='booking-details-container'>
          <h1>{book.room}</h1>
          <h3>Booking-Id:{book.booking_id}</h3>
          <h3>Booking-Date-Time:{moment(book.booking_date_time).format("DD-MM-YYYY , HH:mm:ss")}</h3>
          <h3>Booking-Amount:{book.booking_amount}</h3>
          <h3>Advanced-Amount:{book.booking_advance_amount}</h3>
          <h3>Booking-Status:{book.status==='Open'?"confrimed":"Cancelled"}</h3>
          <div className="cancel-button">
            <button className='btn btn-danger cancel-btn'>
              Cancel-Booking
            </button>
          </div>
        </div>
      }))}
    </div>
  )
}

