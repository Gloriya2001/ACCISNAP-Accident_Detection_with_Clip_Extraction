import React from "react";
import Home from "./pages/Home";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles.css";

const App = () => {
  return (
    <div className="app-container">
      <Navbar />
      <Home />
      <Footer />
    </div>
  );
};

export default App;