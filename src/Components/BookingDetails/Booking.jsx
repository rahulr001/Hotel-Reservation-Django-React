import React, { useState } from "react";
import "./Booking.css";
import { Form, Input } from "semantic-ui-react";
import {  useNavigate } from "react-router-dom";
import moment from "moment";
import axios from 'axios';
import StripeCheckout from 'react-stripe-checkout';
import Loading from "../Loading/Loading";
import Swal from 'sweetalert2';
import generator from 'generate-serial-number';

function Booking({ room, fromdate,todate }) {
  const [error, setError] = useState(false);
  const [error1, setError1] = useState(false);
  const [error2, setError2] = useState(false);
  const [error3, setError3] = useState(false);
  const [loading, setLoading] = useState(false);
  const [success,setSuccess]=useState(false);
  

  const [values, setValues] = useState({
    name: "",
    mobile: "",
    aadhar: "",
    email: "",
  });

  
  const fromDate=moment(fromdate, "DD-MM-YYYY")
  const toDate=moment(todate,"DD-MM-YYYY")
  const totalDays = moment.duration(toDate.diff(fromDate)).asDays()+1;
  const totalAmount =totalDays* room.rentperday*values.noofrooms 
  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((prevalues) => {
      return {
        ...prevalues,
        [name]: value,
      };
    });
    setError(false)
    setError1(false)
    setError2(false)
    setError3(false)
  };

  const validation = () => {
    if (!values.name) {
      return setError(true);
    }
    if (!values.aadhar) {
      return setError1(true);
    }
    if (!values.mobile) {
      return setError2(true);
    }else if(!values.mobile>=10){
      return setError2(true)
    }
    if (!values.email) {
      return setError3(true);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(values);
    validation();
    setValues({
      name: "",
      mobile: "",
      aadhar: "",
      email: "",
      noofrooms:0,
    });
  };
// const bookingDateTime=moment().format('DD-MM-YYYY HH:mm:ss')
const user = JSON.parse(localStorage.getItem("currentUser"));
var username = user.username
var userid =user.id
var serialNumber = generator.generate(5)
var paymentNumber = generator.generate(5)
var bookingid="BK"+serialNumber;
var paymentid="PY"+paymentNumber;
var status =success !== true ?'Open':'Closed'
var datetime=new Date
let dt=moment(datetime).format("DD-MM-YYYY  HH:mm:ss")
console.log(dt)
async function handleBooking (){

  const bookingPersonDetails ={
    user:user.id,
    name:values.name,
    mobile_no:values.mobile,
    adhaar_no:values.aadhar,
    email:values.email
  }
const bookingRoomDetails={
  user:user.id,
  booking_id:bookingid,
  room_type:"Single",
  no_of_rooms:values.noofrooms,
  from_date:fromdate,
  to_date:todate
}
const bookingDetails ={
  user:user.id,
  booking_id:bookingid,
  booking_amount:totalAmount,
  booking_advance_amount:totalAmount,
  booking_status:status
}
const paymentDetails={
  user:user.id,
  payment_id:paymentid,
  amount:totalAmount,
  mode_of_payment:'Card',
  date_time:dt,
  booking_id:bookingid,
  payment_status:"Complete"
}
       
    // axios.post("http://rahulr0001.pythonanywhere.com/hotel/bookingDetails/", bookingDetails)
    // .then(res=>console.log(res.data)) 

try{
   setLoading(true)
    await axios.all([
    axios.post("http://rahulr0001.pythonanywhere.com/hotel/bookingPerson/", bookingPersonDetails), 
    axios.post("http://rahulr0001.pythonanywhere.com/hotel/roomBooking/", bookingRoomDetails),
    axios.post("http://rahulr0001.pythonanywhere.com/hotel/bookingDetails/", bookingDetails),
    axios.post("http://rahulr0001.pythonanywhere.com/hotel/roomPayment/", paymentDetails)
])
  .then(axios.spread((data1, data2, data3,data4) => {
    console.log('data1', data1, 'data2', data2, 'data3', data3, 'data4', data4)
  }));
  setLoading(false)
 
}catch(error){
  setLoading(false)
}

}
let navigate = useNavigate();
function onToken(token){
  Swal.fire("Oops","Something Went Wrong","error" )
  console.log(token);
  Swal.fire("Congratulations","Your Room Booked Successfully","success")
  setSuccess(true);
  handleBooking()
  .then(result=>{
    // window.location.href='/profile';
    let path = `/profile`; 
    navigate(path);
  })
}
return (
    <div className="booking-container">
      <div className="booksub-container">
      <div className="b-left">
          <div className="book-content">
            <div className="room-details">
              <h1>{room.name}</h1>
              <p>Max-Count: {room.maxcount}</p>
              <p>Type: {room.type}</p>
              <p>From-Date: {fromdate}</p>
              <p>To-Date: {todate}</p>
            </div>
            <div className="room-img">
              <img src={room.imageurls[0]} alt="" />
            </div>
          </div>
          <div className="amount">
            <h1>Amount</h1>
            <div className="room-fields">
                <Form.Field
                  control={Input}
                  type="number"
                  label="Number-Of-Rooms:"
                  placeholder="Enter Number of Rooms"
                  name="noofrooms"
                  value={values.noofrooms}
                  onChange={handleChange}
                  // error={error2 && "Please enter a valid Mobile-Number"}
                />
              </div>
            <p>Total-Days: {totalDays}</p>
            <p>Rent-per-day: {room.rentperday}</p>
            <p>Payable-Amount: {!totalAmount ? 0 : totalAmount} </p>
          </div>
        </div>
        <div className="b-right">
          <div className="user-details">
            <Form onSubmit={handleSubmit}>
              <h1>Fill The Details To Book</h1>
              <div className="form-fields">
                <Form.Field
                  control={Input}
                  type="text"
                  label="Full-Name"
                  placeholder="Full-name"
                  name="name"
                  value={values.name}
                  onChange={handleChange}
                  error={
                    error && {
                      content: "Please enter a your name",
                    }
                  }
                />
              </div>
              <div className="form-fields">
                <Form.Field
                  control={Input}
                  type="email"
                  label="E-Mail"
                  placeholder="E-Mail"
                  name="email"
                  value={values.email}
                  onChange={handleChange}
                  error={error3 && "Please enter a Valid Email"}
                />
              </div>
              <div className="form-fields">
                <Form.Field
                  control={Input}
                  type="text"
                  label="Aadhar/Pan"
                  placeholder="Aadhar/Pan"
                  name="aadhar"
                  value={values.aadhar}
                  onChange={handleChange}
                  error={error1 && "Please enter a Valid Aadhar/Pan"}
                />
              </div>
              <div className="form-fields">
                <Form.Field
                  control={Input}
                  type="number"
                  label="Mobile"
                  placeholder="Enter Your Mobile-Number"
                  name="mobile"
                  value={values.mobile}
                  onChange={handleChange}
                  error={error2 && "Please enter a valid Mobile-Number"}
                />
              </div>
              
              <StripeCheckout
              amount={totalAmount * 100}
              currency="INR"
              token={onToken}
              stripeKey="pk_test_51MOKrBSHibQzk1pAthy8jVcwkmmkfyumwvDDqDvzniShMZ5mUDxzWBLjTaOa1Ng0vInbh6SIvGFzRKRLhWGjD0qh003l10aVTb"
             > 
             <button
                type="submit"
                className="btn btn-success submit"
                disabled={
                  !values.name ||
                  !values.mobile ||
                  !values.aadhar ||
                  !values.email
                }
                // onClick={handleBooking}
              >
                Pay-Now
              </button>
               </StripeCheckout>
            </Form>
          </div>
        </div>
       </div>
    </div>
  );
}

export default Booking;
