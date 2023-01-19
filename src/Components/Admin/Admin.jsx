import React, { useEffect, useState } from "react";
import { Tabs } from "antd";
import "./Admin.css";
import axios from "axios";
import { Form, Input } from "semantic-ui-react";
import Table from "react-bootstrap/Table";
import Loading from "../Loading/Loading";
import moment from "moment";
const { TabPane } = Tabs;

function Admin() {
  return (
    <div className="admin-container">
      <div className="admin-header">
        <h1>Admin-Panel</h1>
      </div>
      <Tabs defaultActiveKey="1">
        <TabPane tab="Bookings" key="1">
          <RoomsOccupancy />
        </TabPane>
        <TabPane tab="Rooms" key="2">
          <Bookings />
        </TabPane>
        <TabPane tab="Add-Rooms" key="3">
          <Addroom/>
        </TabPane>
        {/* <TabPane tab="User" key="4">
          <h1>hello</h1>
        </TabPane> */}
      </Tabs>
    </div>
  );
}

export default Admin;

export function Bookings() {
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(false);
  const user = JSON.parse(localStorage.getItem("currentUser"));
  const getdata = () => {
    try {
      setLoading(true);
      axios
        .get("http://rahulr0001.pythonanywhere.com/hotel/roomBookingDetails/")
        .then((res) => {
          console.log(res.data);
          setBookings(res.data);
        });
      setLoading(false);
    } catch (error) {
      setLoading(false);
      console.log(error);
    }
  };
  useEffect(() => {
    getdata();
  }, []);
  return (
    <div>
      <Table striped bordered hover>
        <thead class="table-danger">
          <tr>
            <th>Booking_id</th>
            <th>Booking-Date-Time</th>
            <th>Booking-Amount</th>
            <th>Advanced-Amount</th>
            <th>Booking-Status</th>
          </tr>
        </thead>
        <tbody>
          {bookings.map((book) => (
            <tr>
              <td>{book.booking_id}</td>
              <td>
                {moment(book.booking_date_time).format("DD-MM-YYYY , HH:mm:ss")}
              </td>
              <td>{book.booking_amount}</td>
              <td>{book.booking_advance_amount}</td>
              <td>{book.status === "Open" ? "confrimed" : "Cancelled"}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export function RoomsOccupancy() {
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(false);
  const user = JSON.parse(localStorage.getItem("currentUser"));
  const getdata = () => {
    try {
      setLoading(true);
      axios
        .get("http://rahulr0001.pythonanywhere.com/hotel/roomOccupancy/")
        .then((res) => {
          console.log(res.data);
          setBookings(res.data);
        });
      setLoading(false);
    } catch (error) {
      setLoading(false);
      console.log(error);
    }
  };
  useEffect(() => {
    getdata();
  }, []);
  return (
    <div>
      <Table striped bordered hover responsive>
        <thead class="table-danger">
          <tr>
            <th>Booking_id</th>
            <th>User</th>
            <th>Room-Type</th>
            <th>No of Rooms</th>
            <th>From-Date</th>
            <th>To-date</th>
          </tr>
        </thead>
        <tbody>
          {bookings.map((book) => (
            <tr>
              <td>{book.booking_id}</td>
              <td>{book.user}</td>
              <td>{book.room_type}</td>
              <td>{book.no_of_rooms}</td>
              <td>{book.from_date}</td>
              <td>{book.to_date}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}




export function Addroom() {
  const[values,setValues]=useState({})
  const [loading, setLoading] = useState(false);
  const user = JSON.parse(localStorage.getItem("currentUser"));

  const postdata = () => {
    try {
      setLoading(true);
      axios
        .post("url")
        .then((res) => {
          console.log(res.data);
        });
      setLoading(false);
    } catch (error) {
      setLoading(false);
      console.log(error);
    }
  };
  return (
    <div className="addroom-container">
    <div className="form-container">
    <div className="form-fieldss">
            <Form.Field
              control={Input}
              type="text"
              label="RoomName"
              placeholder="RoomName"
              name="roomname"
              // value={values.username}
              // onChange={handleChange}
            />
          </div>
          <div className="form-fieldss">
            <Form.Field
              control={Input}
              type="text"
              label="Room-Type"
              placeholder="Room-Type"
              name="roomtype"
              // value={values.username}
              // onChange={handleChange}
            />
          </div>
          <div className="form-fieldss">
            <Form.Field
              control={Input}
              type="text"
              label="Image-URL1"
              placeholder="Image-URL1"
              name="image_url1"
              // value={values.username}
              // onChange={handleChange}
            />
          </div>
          <div className="form-fieldss">
            <Form.Field
              control={Input}
              type="text"
              label="Image-URL2"
              placeholder="Image-URL2"
              name="image_url2"
              // value={values.username}
              // onChange={handleChange}
            />
          </div>
          <div className="form-fieldss">
            <Form.Field
              control={Input}
              type="text"
              label="Image-URL3"
              placeholder="Image-URL3"
              name="image_url3"
              // value={values.username}
              // onChange={handleChange}
            />
          </div>
          <div className="form-fieldss">
            <Form.Field
              control={Input}
              type="text"
              label="Room-Description"
              placeholder="Room-Description"
              name="room_description"
              // value={values.username}
              // onChange={handleChange}
            />
          </div>
          <button className="btn btn-success upload">Upload</button>
    </div>
    </div>
  )
}

