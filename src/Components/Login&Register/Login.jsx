import React, { useState} from "react";
import { Form, Input } from "semantic-ui-react";
import "./Login-Register.css";
import axios from 'axios';
import Loading from '../Loading/Loading';
import { Link,redirect,useNavigate } from "react-router-dom";
import Swal from 'sweetalert2';

export default function Login() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [success,setSuccess]= useState(false);
  const [values, setValues] = useState({
    username: "",
    password: "",
  });
  let navigate = useNavigate();
  async function login() {
    localStorage.removeItem("currentUser");
    let path = `/home`; 
    await navigate(path);
    // window.location.href = "/login";
  }
  

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((prevalues) => {
      return {
        ...prevalues,
        [name]: value,
      };
    });
    setError(false)
  };
  
  async function postdata(){
    const userdata={
      username:values.username,
      password1:values.password
    }
    try{
      setLoading(true)
    if(Object.values(values).includes("") === false){
      const usersdata = await axios.post('http://rahulr0001.pythonanywhere.com/accounts/login/',userdata)
      localStorage.setItem('currentUser',JSON.stringify(usersdata.data))
      // console.log(localStorage.setItem('currentUser',JSON.stringify(usersdata.data)))
     
      setLoading(false)
      setSuccess(true)
      window.location.href = "/home";
      // login()
    }
  }catch(error){
    console.log(error);
    setLoading(false)
    setError(true)
  }
}


  const handleSubmit = (event) => {
    event.preventDefault();
    postdata()
    // console.log(values);
    // console.log(data);
    setValues({
      username: "",
      password: "",
    });
  };

  return (
    <div className="register-container">
       <div className="load">
      {success &&  Swal.fire("Successfully","Logged-In","success" )}
      {loading && <Loading/>}
      {error &&  Swal.fire("Ivalid-Credentials","Kindly Register","error") && <redirect to='/login'/>}
      </div>
      <div className="register-details login-con">
        <div className="register-header">
          <h1>Login</h1>
        </div>
        <Form className="register-form" onSubmit={handleSubmit}>
        
        
          <h6>Please Enter Your Details to Login</h6>
          <div className="form-fields">
            <Form.Field
              
              control={Input}
              type="text"
              label="UserName"
              placeholder="UserName"
              name="username"
              value={values.username}
              onChange={handleChange}
            />
          </div>
          <div className="form-fields">
            <Form.Field
             
              control={Input}
              type="password"
              label="Password"
              placeholder="Password"
              name="password"
              value={values.password}
              onChange={handleChange}
            />
          </div>
          <div className="register-link">
            <h5>To Register Click <Link to='/register'>here</Link></h5>
          </div>
          <button
           disabled={
            !values.username ||
            !values.password
          }
            className="btn btn-primary register-btn"
            >
            Login
          </button>
        </Form>
      </div>
    </div>
  );
}
