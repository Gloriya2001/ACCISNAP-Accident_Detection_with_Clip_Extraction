import React, { useState } from "react";
import axios from "axios";
import Loader from "./Loader";

const UploadForm = ({ setResult }) => {
  const [video, setVideo] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setVideo(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!video) {
      alert("Please select a video file.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("video", video);

    try {
      const response = await axios.post("http://localhost:8000/api/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error uploading video", error);
      alert("Error processing video");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="text-center">
      <input className="form-control w-50 d-inline" type="file" accept="video/*" onChange={handleFileChange} />
      <button className="btn btn-primary mt-2" onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Detect"}
      </button>
      {loading && <Loader />}
    </div>
  );
};

export default UploadForm;