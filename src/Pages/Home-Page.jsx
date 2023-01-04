import React, { useState, useEffect } from "react";
import axios from "axios";
import Rooms from "../Components/Rooms/Rooms"

function HomePage() {
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState();
  const [error, setError] = useState();

  async function getData() {
    try {
      setLoading(true);
      const data = (
        await axios.get("http://localhost:5000/api/rooms/getallrooms")
      ).data;
      setRooms(data);
      setLoading(false);
       console.log(data)
    } catch (error) {
      setError(true);
      console.log("error");
      setLoading(false);
    }
  }

  useEffect(() => {
    getData();
  }, []);

  return (
    <div>
      <div className="row">
        {loading ? (
          <h1>Loading...</h1>
        ) : error ? (
          <h1>Error...</h1>
        ) : (
          rooms.map((room) => {
            return <div className="col-md-9">
                <Rooms rooms={room}/>
            </div>;
          })
        )}
      </div>
    </div>
  );
}

export default HomePage;
