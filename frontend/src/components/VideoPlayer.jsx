import React from "react";

const VideoPlayer = ({ result }) => {
  return (
    <div>
      <h2>Detection Result</h2>
      <p><strong>Timestamp:</strong> {result.timestamp}</p>
      <video controls>
        <source src={result.clip_url} type="video/mp4" />
      </video>
    </div>
  );
};

export default VideoPlayer;

