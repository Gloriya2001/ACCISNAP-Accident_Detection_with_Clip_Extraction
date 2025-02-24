import React, { useState } from "react";
import UploadForm from "../components/UploadForm";
import VideoPlayer from "../components/VideoPlayer";

const Home = () => {
  const [result, setResult] = useState(null);

  return (
    <div className="container mt-4">
      <h2 className="text-center">Upload a Video for Accident Detection</h2>
      <p className="text-center">Our AI-powered system will analyze the video and extract accident clips.</p>
      <UploadForm setResult={setResult} />
      {result && <VideoPlayer result={result} />}
    </div>
  );
};

export default Home;