import './App.css';
import Navbar from './Components/NavBar/Navbar';
import Rooms from './Components/Rooms/Rooms';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import HomePage from './Pages/Home-Page';
import BookingPage from './Pages/Booking-Page';


function App() {
  return (
    <div className="App">
      <Router>
      <Navbar/>
      <Routes>
        <Route path='/home' element={<HomePage/>}/>
        <Route path='/rooms' element={<Rooms/>}/>
        <Route path='/book/:roomid' element={<BookingPage/>} />
        </Routes>  
      </Router>
      
    </div>
  );
}

export default App;
