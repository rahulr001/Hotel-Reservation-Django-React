import React, { useState, useEffect } from "react";
import axios from "axios";
import Rooms from "../Components/Rooms/Rooms";
import Loading from "../Components/Loading/Loading";
import Error from "../Components/Loading/Error";
import moment from "moment";
import { DatePicker } from "antd";
import { Form, Input, Select } from "semantic-ui-react";

const { RangePicker } = DatePicker;
function RoomPage() {
  const [fromdate, setFromdate] = useState();
  const [todate, setTodate] = useState();
  const [rooms, setRooms] = useState([]);
  const [temproom, setTempRoom] = useState([]);
  const [loading, setLoading] = useState();
  const [error, setError] = useState();

  async function getData() {
    try {
      setLoading(true);
      const data = (
        await axios.get("http://localhost:5000/api/rooms/getallrooms")
      ).data;
      setRooms(data);
      setTempRoom(data);
      setLoading(false);
      //  console.log(data)
    } catch (error) {
      setError(true);
      console.log("error");
      setLoading(false);
    }
  }
  useEffect(() => {
    getData();
  }, []);

  const filterByDate = (dates) => {
    setFromdate(moment(dates[0].$d).format("DD-MM-YYYY"));
    setTodate(moment(dates[1].$d).format("DD-MM-YYYY"));

    var temp = [];
    var availability = false;
    for (const room of temproom) {
      if (room.status === "closed") {
        for (const booking of room.status) {
          if (
            !moment(moment(dates[0].$d).format("DD-MM-YYYY")).isBetween(
              booking.fromdate,
              booking.todate
            ) &&
            !moment(moment(dates[1].$d).format("DD-MM-YYYY")).isBetween(
              booking.fromdate,
              booking.todate
            )
          ) {
            if (
              moment(dates[0].$d).format("DD-MM-YYYY") !== booking.fromdate &&
              moment(dates[0].$d).format("DD-MM-YYYY") !== booking.todate &&
              moment(dates[1].$d).format("DD-MM-YYYY") !== booking.fromdate &&
              moment(dates[1].$d).format("DD-MM-YYYY") !== booking.todate
            ) {
              availability = true;
            }
          }
        }
      }
      if (availability === true || room.status === "open") {
        temp.push(rooms);
      }
      setTempRoom(temp);
    }
  };
  const roomOption = [
    { key: "all", value: "all", text: "All" },
    { key: "delux", value: "delux", text: "Delux" },
    { key: "non-delux", value: "non-delux", text: "Non-Delux" },
    { key: "luxary", value: "luxary", text: "Luxary" },
  ];
  const [search, setSearch] = useState("");
  

  function filterBySearch() {
    const temp = temproom.filter((room) =>
      room.name.toLowerCase().includes(search.toLowerCase())
    );
    setRooms(temp);
  }

  function filterBytype(e,data) {
    if(data.value!=='all'){
    const temp = temproom.filter(
      (room) => room.type.toLowerCase() === data.value.toLowerCase()
    )
    setRooms(temp);
  }else{
    setRooms(temproom);
  }
  }

  return (
    <div className="main-content">
      {/* <div className="img-bg">
        <img
          src="https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
          alt=""
        />
      </div> */}
      <div className="roompage-container">
        <div className="search-container">
          <div className="search-bg">
          </div>
            <div className="left-box">
            <h3>Search to Find Rooms</h3>
            <RangePicker
              className="datepicker"
              format="DD-MM-YYYY"
              onChange={filterByDate}
            />
            <div className="search-fields">
              <Select
                placeholder="Select your Room-Type"
                options={roomOption}
                onChange={filterBytype}
              />
            </div>
            <div className="search-fields box">
              <Form.Field
                control={Input}
                type="text"
                // label="Full-Name"
                placeholder="Search-Rooms"
                name="name"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                onKeyUp={filterBySearch}
              />
            </div>
          </div>
        </div>
        <div className="gallery-container">
          {loading ? (
            <Loading />
          ) : (
            rooms.map((room) => {
              return (
                <div className="">
                  <Rooms rooms={room} fromdate={fromdate} todate={todate} />
                </div>
              );
            })
          )}
        </div>
      </div>
    </div>
  );
}

export default RoomPage;
