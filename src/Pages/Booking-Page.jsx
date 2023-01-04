import React,{useEffect,useState} from 'react';
import axios from 'axios'; 
import { useParams } from 'react-router-dom';
import Booking from '../Components/BookingDetails/Booking';


function BookingPage({match}) {
    const {roomid} = useParams();
    const [room, setRoom] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState();

    async function postData() {
        try {
          setLoading(true);
          const data = (
            await axios.post("http://localhost:5000/api/rooms/getroombyid",{roomid:roomid})
          ).data;
          setRoom(data);
          setLoading(false);
           console.log(data)
        } catch (error) {
          setError(true);
          console.log("error");
          setLoading(false);
        }
      }
    
      useEffect(() => {
        postData();
      },[]);
    
  return (
    <div>
      <div className="row">
        {loading ? (
          <h1>Loading...</h1>
        ) : error ? (
          <h1>Error...</h1>
        ) : (
            <div className='main-con'>
                <Booking room={room}/>
            </div>
        )}
      </div>
    </div>
  )
}

export default BookingPage;