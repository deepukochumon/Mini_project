import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HelloWorld from './Helloworld.js';
import SignUpForm from './components/SignUpForm.js';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<SignUpForm />} />
        <Route path="/hello" element={<HelloWorld />} />
      </Routes>
    </Router>
  );
}

export default App;