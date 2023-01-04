import React from "react";
import "./Navbar.css";
import "../../App.css";
import { Link } from "react-router-dom";
import { useState } from "react";
// import {FaTimes, FaBars} from 'react-icons/fa';
const Routes = [
  {
    path: "/home",
    name: "Home",
    // icon: <FaHome />,
  },
  {
    path: "/rooms",
    name: "Enq-Form",
    // icon: <FaWpforms />,
  },
  {
    path: "/enqlist",
    name: "Enq-List",
    // icon: <FaList />,
  },
  {
    path: "/enqfilterlist",
    name: "FollowUp-List",
    // icon: <FaListAlt />,
  },
];

const Navbar = () => {
  const [click, setClick] = useState(false);


  const handleClick = () => setClick(!click);
  return (
    <div className="n-wrapper" id="Navbar">
      <div className="n-left">
        <div className="n-name">
          <h1 className="profile-name">VR-Rooms</h1>
        </div>
      </div>
      <div className="n-right">
        <div className="n-list">
          <ul className={click ? "nav-menu active" : "nav-menu"}>
          <li><Link className='link' to="">
              Register
            </Link></li>
            <li><Link className='link' to="Education">
              Login
            </Link></li>
            <li><Link className='link' to="home">
              Home
            </Link></li>
            {/* <Link
              spy={true}
              to="Experience"
              smooth={true}
              activeClass="activeClass"
            >
              <li>Experience</li>
            </Link>
            <Link
              spy={true}
              to="Projects"
              smooth={true}
              activeClass="activeClass"
            >
              <li>Projects</li>
            </Link>
            <Link
              spy={true}
              to="Testimonials"
              smooth={true}
              activeClass="activeClass"
            >
              <li>Testimonials</li>
            </Link> */}
          </ul>
          <div className="nav-icons" onClick={handleClick}>
            <i
              className={click ? " button fas fa-times" : " button fas fa-bars"}
            ></i>
          </div>
        </div>

        <Link spy={true} to="Contact" smooth={true} activeClass="activeClass">
          <button className="button n-button">Contact</button>
        </Link>
      </div>
    </div>
  );
};
export default Navbar;
