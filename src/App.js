import './App.css';
import 'semantic-ui-css/semantic.min.css';
import 'antd/dist/reset.css';
import Navbar from './Components/NavBar/Navbar';
import Rooms from './Components/Rooms/Rooms';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import RoomPage from './Pages/Room-Page';
import BookingPage from './Pages/Booking-Page';
import Login from './Components/Login&Register/Login';
import Register from './Components/Login&Register/Register';
import Profile from './Components/Profile/Profile';
import Admin from './Components/Admin/Admin';
import ViewDetails from './Components/viewdetails/viewDetails';
import Home from './Components/Home/Home';



function App() {
  return (
    <div className="App">
      <Router>
      <Navbar/>
      <Routes>
        <Route path='/home' element={<Home/>} />
        <Route path='/roompage' element={<RoomPage/>}/>
        <Route path='/rooms' element={<Rooms/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/book/:roomid/:fromdate/:todate' element={<BookingPage/>} />
        <Route path='/profile' element={<Profile/>}/>
        <Route path='/admin' element={<Admin/>}/>
        <Route path='/viewdetails/:roomid/:fromdate/:todate' element={<ViewDetails/>}/>
        </Routes>  
      </Router>
      
    </div>
  );
}

export default App;
