import React, { useState } from "react";
import "./style.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function SignUpForm() {
  const [isSignIn, setIsSignIn] = useState(true);
  const [username, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate()

  const toggleForm = () => {
    setIsSignIn(!isSignIn);
  };

  const handleSwipe = (e) => {
    if (e.deltaX > 0) {
      setIsSignIn(false);
    } else {
      setIsSignIn(true);
    }
  };

  const handleSignIn = async (e, user_type) => {
    e.preventDefault();
    
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/myapi/login/",
        {
          username: username,
          password: password,
          user_type: user_type,
        }
      );

      console.log(response.data);// Handle successful login response
      const baseurl='http://localhost:3000';
      let redirecturl=response.data.redirect_url;

      //const isAbsoluteUrl = redirecturl.startsWith("http://") || redirecturl.startsWith("https://");

     // if (!isAbsoluteUrl) {
        // Construct absolute URL from relative path
       // redirecturl = new URL(redirecturl, baseurl).toString();
     // }
    
     window.location.href = redirecturl;

      setEmail("");
      setPassword("");
    } catch (error) {
      console.error("Error:", error); // Handle error
      console.log('invalid credentials')
      if (error.response && error.response.data && error.response.data.message) {
        setErrorMessage(error.response.data.message);
      } else {
        setErrorMessage("An error occurred. Please try again later.");
      }
    }
  };

  return (
    <div className="viewport-container">
    {errorMessage && (
      <div className="error-message" style={{ 'padding-left':'42%','color':'red'}}>
        <p>{errorMessage}</p>
      </div>
    )}
    <div
    className={`container ${isSignIn ? "" : "right-panel-active"}`}
    id="container"
    >
      <div className="form-container sign-up-container">
        <form action="#" method="post">
          <h1>Faculty Login</h1>
          <div className="social-container">
            <a href="#" className="social">
              <i className="fab fa-facebook-f"></i>
            </a>
            <a href="#" className="social">
              <i className="fab fa-google-plus-g"></i>
            </a>
            <a href="#" className="social">
              <i className="fab fa-linkedin-in"></i>
            </a>
          </div> 
          <span>or use your email for registration</span>
          <input type="text" placeholder="Email" value={username} onChange={(e) => setEmail(e.target.value)}/>
          <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
          <button type="submit"  onClick={ (e) => handleSignIn(e,'faculty')} >Sign In</button>
        </form>
      </div>
      <div className="form-container sign-in-container">
        <form action="#" method="post">
          <h1>Student Login</h1>
          <div className="social-container">
            <a href="#" className="social">
              <i className="fab fa-facebook-f"></i>
            </a>
            <a href="#" className="social">
              <i className="fab fa-google-plus-g"></i>
            </a>
            <a href="#" className="social">
              <i className="fab fa-linkedin-in"></i>
            </a>
          </div>
          <span>or use your account</span>
         
          <input type="text" placeholder="Email" value={username} onChange={(e) => setEmail(e.target.value)}/>
          <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
          <a href="#">Forgot your password?</a>
          <button type="submit" onClick={ (e) => handleSignIn(e,'student')} >Sign In</button>
        </form>
      </div>
      <div className="overlay-container">
        <div className="overlay">
          <div className="overlay-panel overlay-left">
            <h1>Are you a Student?</h1>
            <p>Then please try this student login</p>
            <button className="ghost" onClick={toggleForm} id="signIn" type="button">
              Sign In
            </button>
          </div>
          <div className="overlay-panel overlay-right">
            <h1>Are You a Faculty?</h1>
            <p>Then Use this Faculty Login page</p>
            <button type="button" className="ghost" onClick={toggleForm} id="signIn">
              Sign In
            </button>
          </div>
        </div>
      </div>
    </div>
    </div>
  );
}

export default SignUpForm;
