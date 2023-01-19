import React, { useState } from "react";
import { Form, Input } from "semantic-ui-react";
import "./Login-Register.css";
import axios from 'axios';
import Loading from '../Loading/Loading';
import { Link } from "react-router-dom";
 



function Register() {

  const [error0, setError0] = useState(false);
  const [error1, setError1] = useState(false);
  const [error2, setError2] = useState(false);
  const [error3, setError3] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [success,setSuccess]= useState(false);


  const [values, setValues] = useState({
    username: "",
    email: "",
    password1: "",
    password2: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((prevalues) => {
      return {
        ...prevalues,
        [name]: value,
      };
    });
    setError0(false)
    setError1(false)
    setError2(false)
    setError3(false)
    setSuccess(false)
    setError(false)
  };

  const validation = () => {
    if (!values.username) {
      return setError0(true);
    }
    if (!values.email) {
      return setError1(true);
    }
    if (!values.password1) {
      return setError2(true);
    } 
    if (!values.password2) {
      return setError3(true);
    } else if (values.password1 !== values.password2) {
      return setError3(true);
    }
  };

async function postdata (){
  const userdata={
    username:values.username,
    email:values.email,
    password1:values.password1,
    password2:values.password2
  }
  try{
    setLoading(true)
  if(error0||error1||error2||error3 === false){
    await axios.post('http://rahulr0001.pythonanywhere.com/accounts/register/',userdata) 
    .then(res=>console.log(res.data))
    setLoading(false)
    setSuccess(true)
  }}catch(error){
      console.log(error);
      setLoading(false)
      setError(true)
  }
  
}
  const handleSubmit = (event) => {
    event.preventDefault();
     postdata()

    setValues({
      username: "",
      email: "",
      password1: "",
      password2: "",
    });
    validation();
  };

  return (
    <div className="register-container">
      <div className="load">
      {loading && <Loading/>}
      </div>
      <div className="register-details">
        <div className="register-header">
          <h1>Register</h1>
        </div>
        <Form className="register-form" onSubmit={handleSubmit}>
          {error && <h6 style={{color:'red',fontSize:'1rem'}}>Something Went Wrong</h6>}
          {success && <h6 style={{color:'green',fontSize:'1rem'}}>Successfully Registered</h6>}
          <h6>Please Enter Your Details to Register</h6>
          <div className="form-fields">
            <Form.Field
              control={Input}
              type="text"
              label="UserName"
              placeholder="UserName"
              name="username"
              value={values.username}
              onChange={handleChange}
              error={
                error0 && {
                  content: "Please enter Username",
                  position: "top",
                }
              }
            />
          </div>
          <div className="form-fields">
            <Form.Field
              control={Input}
              type="text"
              label="Email-ID"
              placeholder="Email-ID"
              name="email"
              value={values.email}
              onChange={handleChange}
              error={
                error1 && {
                  content: "Please enter a your Email",
                  position: "top",
                }
              }
            />
          </div>
          <div className="form-fields">
            <Form.Field
              control={Input}
              type="password"
              label="Password"
              placeholder="Password"
              name="password1"
              value={values.password1}
              onChange={handleChange}
              error={
                error2 && {
                  content: "Please enter a your Password",
                  position: "top",
                }
              }
            />
          </div>
          <div className="form-fields">
            <Form.Field
              control={Input}
              type="password"
              label="Confrim-Password"
              placeholder="Confrim Password"
              name="password2"
              value={values.password2}
              onChange={handleChange}
              error={
                error3 && {
                  content: "Confrim-Password Should Match",
                  position: "top",
                }
              }
            />
          </div>
          <button
            disabled={
              !values.username ||
              !values.email ||
              !values.password1 ||
              !values.password2
            }
            className="btn btn-primary register-btn"
          >
            Register
          </button>
          <div className="register-link">
            <h5>To Login Click <Link to='/login'>here</Link></h5>
          </div>
        </Form>
      </div>
    </div>
  );
}

export default Register;
