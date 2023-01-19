import React,{useEffect,useState} from 'react';
import axios from 'axios'; 
import { useParams } from 'react-router-dom';
import Booking from '../Components/BookingDetails/Booking';
import Loading from '../Components/Loading/Loading';
import Error from '../Components/Loading/Error';
import Success from '../Components/Loading/Success';


function BookingPage({match}) {
    const {roomid,fromdate,todate} = useParams();
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
          //  console.log(data)
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
          <Loading/>
        ) : room ? (
          <div className='main-con'>
                <Booking room={room} fromdate={fromdate} todate={todate}/>
            </div>
          ) : (
            <Error/>
        )}
      </div>
    </div>
  )
}

export default BookingPage;