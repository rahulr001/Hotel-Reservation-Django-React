import React, { useEffect, useState } from "react";
import "./viewDetails.css";
import { useParams } from "react-router-dom";
import axios from "axios";
import {Link, useNavigate } from 'react-router-dom';
import Loading from "../Loading/Loading";
import Error from "../Loading/Error";
import { Carousel } from "react-bootstrap";
import { DatePicker } from "antd";
import {FaWifi,FaTv,FaDoorClosed} from 'react-icons/fa';
import moment from "moment";
import dayjs from 'dayjs';


const { RangePicker } = DatePicker;
function ViewDetails() {
  const { roomid, fromdate, todate } = useParams();
  const [room, setRoom] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState();
  const[fromdates,setFromdates]=useState();
  const[todates,setTodates]=useState()
  const user = JSON.parse(localStorage.getItem("currentUser"));
 
 
  

  async function postData() {
    try {
      setLoading(true);
      const data = (
        await axios.post("http://localhost:5000/api/rooms/getroomdetailsbyid", {
          roomid: roomid,
        })
      ).data;
      setRoom(data);
      setLoading(false);
    } catch (error) {
      setError(true);
      console.log("error");
      setLoading(false);
    }
  }
  let fdate=fromdate
  let tdate=todate
  let date1 = moment(fdate,"DD-MM-YYYY")._i
  let date2 = moment(tdate,"DD-MM-YYYY")._i
  function datess(){
    return[date1,date2]
  }
  function filterByDates(dates){
    if(moment(dates[0]).format("DD-MM-YYYY")===""){
       setFromdates(moment(fdate,"DD-MM-YYYY")._i)
    }
    if(moment(dates[1]).format("DD-MM-YYYY")===""){
      setTodates(moment(tdate,"DD-MM-YYYY")._i)
   }else{
    setFromdates(moment(dates[0].$d).format("DD-MM-YYYY"));
    setTodates(moment(dates[1].$d).format("DD-MM-YYYY"));
  }
  moment(dates[1]).format("DD-MM-YYYY")
 }
 function filterByDate(dates){
  
  setFromdates(moment(dates[0].$d).format("DD-MM-YYYY"));
  setTodates(moment(dates[1].$d).format("DD-MM-YYYY"));


}
  console.log(fromdates)
  console.log(todates)
  
  useEffect(() => {
    postData();
     }, []);

  return (
    <div className="viewdetails-container">
      <div className="row">
        {loading ? (
          <Loading />
        ) : room ? (
          <div className="carousel-con">
            <div className="carousel">
              <Carousel className="carousel-img" fade>
              {room.imageurls.map((url) => {
                return (
                  <Carousel.Item >
                    <img className="carousel-image" src={url} alt="" />
                  </Carousel.Item>
                );
              })}
            </Carousel>
            </div>
            <div className="carousel-details">
              <div className="carousel-left">
                <h1>{room.name}</h1>
                <h1>Descripition</h1>
                <p>{room.description}</p>
                <h1>Amenties</h1>
                <h6>{<div className='room-icons'><FaWifi/>&emsp;<FaTv/>&emsp;<FaDoorClosed/></div>}</h6>
                </div>
                <div className="carousel-right">
                  <div className="carousel-right-header">
                    <h1>Book-Details</h1>
                  </div>
                <RangePicker
                className="dp"
                 format="DD-MM-YYYY"
                 defaultValue={[dayjs(fdate,"DD-MM-YYYY"),dayjs(tdate,"DD-MM-YYYY")]}
                 onChange={filterByDate}
                />
                <h5><FaDoorClosed/>&emsp;{room.type}</h5>
                <h5>10% off on Every Booking </h5>
                 <Link to={user?`/book/${room._id}/${fromdate}/${todate}`:"/login"}>
                <button className="btn btn-success bookbtn">Book-Now</button>
                </Link> 
              </div>
            </div>
          </div>
        ) : (
          <Error />
        )}
      </div>
    </div>
  );
}

export default ViewDetails;
