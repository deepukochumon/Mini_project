import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FormComponent = () => {
  const [formData, setFormData] = useState({
    class_s: '',
    s_no: null,
    e_no: null,
    date: null,
    batch: '',
    diary: [],
    classes: [],
    batches_selected: []
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/myapi/attendance_query/");
        setFormData(response.data);
      } catch (error) {
        console.error("Error fetching user data:", error);
        console.log('error occured')
        // Handle error: Display error message to user or retry fetch
      }
    };
    fetchData();
  }, []);

  return (
    <form>
      <label>Class:</label>
      <select name="class_s" value={formData.class_s || ''}>
        {formData.classes.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>

      <label>Batch:</label>
      <select name="batch" value={formData.batch || ''}>
        {formData.batches_selected.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>

      <label>Diary:</label>
      <select name="diary" value={formData.diary[0] || ''}>
        {formData.diary.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>

      {/* Render other form fields similarly */}
      <button type="submit">Submit</button>
    </form>
  );
};

export default FormComponent;
