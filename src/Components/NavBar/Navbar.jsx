import React from "react";
import "./Navbar.css";
import "../../App.css";
import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import { FaUser } from "react-icons/fa";
// import {FaTimes, FaBars} from 'react-icons/fa';

const Navbar = () => {
  const [click, setClick] = useState(false);
  const user = JSON.parse(localStorage.getItem("currentUser"));
  // console.log(user.username)
  // console.log(user.password)
  let navigate = useNavigate();
  function logout() {
    localStorage.removeItem("currentUser");
    let path = `/login`; 
    navigate(path);
    // window.location.href = "/login";
  }
  function booking(){
    let path = `/profile`; 
    navigate(path);
  }

  const handleClick = () => setClick(!click);
  return (
    <div className="nav-container">
      <div className="n-wrapper" id="Navbar">
        <div className="n-left">
          <div className="n-name">
            <h1 className="profile-name">LOGO</h1>
          </div>
        </div>
        <div className="n-right">
          <div className="n-list">
            <ul className={click ? "nav-menu active" : "nav-menu"}>
              <li>
                <Link className="link" to="home">
                  Home
                </Link>
              </li>
              {user ? (
                <div className="nav-corner">
                  <Dropdown className="dropdown">
                    <Dropdown.Toggle className='dropdown-btn' variant="light" id="dropdown-basic">
                      <FaUser /> {user.username}
                    </Dropdown.Toggle>

                    <Dropdown.Menu>
                      <Dropdown.Item  className='dropdown-item' onClick={booking}>Bookings</Dropdown.Item>
                      <Dropdown.Item className='dropdown-item' onClick={logout}>Log-Out</Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                </div>
              ) : (
                <div className="nav-corner">
                  {/* <li>
                    <Link className="link" to="register">
                      Register
                    </Link>
                  </li> */}
                  <li>
                    <Link className="link" to="login">
                      Login/Register
                    </Link>
                  </li>
                </div>
              )}

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
                className={
                  click ? " button fas fa-times" : " button fas fa-bars"
                }
              ></i>
            </div>
          </div>

          {/* <Link spy={true} to="Contact" smooth={true} activeClass="activeClass">
          <button className="button n-button">Contact</button>
          </Link> */}
        </div>
      </div>
    </div>
  );
};
export default Navbar;
