import React, { useState, useEffect } from "react";
import axios from "axios";
import styles from "./Home.module.css"; // Update the import statement
import profileImage from "../static/profile-1.jpg";
import { Link } from "react-router-dom";
import { type } from "@testing-library/user-event/dist/type";

function Home() {
  const [userData, setUserData] = useState(null);
  const [labsData, setLabsData] = useState([]);

  useEffect(() => {
    // Fetch user data from the backend
    const fetchUserData = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/myapi/user-data/"
        );
        setUserData(response.data);
        const labsResponse = await axios.get(
          "http://127.0.0.1:8000/myapi/lab-details/"
        );
        setLabsData(labsResponse.data.lab_names);
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    };

    fetchUserData();
  }, []);

  return (
    <div>
      <header className={styles.header}>
        <div className={styles.logo} title="University Management System">
          <h2>
            S<span className={styles.danger}>T</span>UDENT D
            <span className={styles.danger}>A</span>SHBOARD
          </h2>
        </div>
        <div className={styles.navbar}>
          <a href="index.html" className={styles.active}>
            <span className="material-icons-sharp">home</span>
            <h3>Home</h3>
          </a>
          <a href="marks.html ">
            <span className="material-icons-sharp">today</span>
            <h3>Marks</h3>
          </a>
          <a href="doubts.html">
            <span className="material-icons-sharp">grid_view</span>
            <h3>Doubts</h3>
          </a>
          <a href="password.html">
            <span className="material-icons-sharp">password</span>
            <h3>Change Password</h3>
          </a>
          <a href="#">
            <Link to="/login">
              <span className="material-icons-sharp">logout</span>
              <h3>Logout</h3>
            </Link>
          </a>
        </div>
        <div id="profile-btn" className={styles.profileBtn}>
          <span className="material-icons-sharp">person</span>
        </div>
        <div className={styles.themeToggler}>
          <span className="material-icons-sharp active">light_mode</span>
          <span className="material-icons-sharp">dark_mode</span>
        </div>
      </header>
      <div className={styles.container}>
        <aside>
          <div className={styles.profile}>
            <div className={styles.top}>
              <div className={styles.profile_photo}>
                <img src={profileImage} alt="Profile" />
              </div>
              <div className={styles.info}>
                <p>
                  Hey, <b>{userData ? userData.name : "Loading..."}</b>
                </p>
                <small className={styles.textMuted}>12102030</small>
              </div>
            </div>
            <div className={styles.about}>
              <h5>Course</h5>
              <p>
                {userData ? userData.department : "Loading..."},S
                {userData ? userData.sem : "Loading..."}
              </p>

              <h5>DOB</h5>
              <p>{userData ? userData.dob : "Loading..."}</p>
              <h5>Phone Number</h5>
              <p>{userData ? userData.phone : "Loading..."}</p>
              <h5>Email</h5>
              <p>{userData ? userData.email : "Loading..."}</p>
              <h5>Address</h5>
              <p>Ghost town Road, New York, America</p>
            </div>
          </div>
        </aside>

        <main>
          <h1 style={{ fontWeight: 800, fontSize: "1.8rem" }}>Attendance</h1>

          <div>
            {labsData.map((lab, index) => (
              <div className={styles.subjects}>
                <div>
                  <h1>{lab}</h1>
                  <p>
                    <div className={styles.percent}>
                      <b>96%</b>
                    </div>
                  </p>
                </div>
              </div>
            ))}
          </div>

          <div className={styles.timetable} id="timetable">
            {/* Add your timetable component here */}
          </div>
        </main>

        <div className={styles.right}>
          <div className={styles.announcements}>
            <h2 style={{ marginBottom: "0.8rem" }}>Announcements</h2>
            <div className={styles.updates}>
              {/* Add your announcements components here */}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
