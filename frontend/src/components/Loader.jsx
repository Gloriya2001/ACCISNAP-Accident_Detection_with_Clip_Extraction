import React from "react";

const Loader = () => {
  return (
    <div className="text-center mt-3">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Processing...</span>
      </div>
      <p>Processing video, please wait...</p>
    </div>
  );
};

export default Loader;