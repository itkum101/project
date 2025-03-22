import React from 'react';
import './HomePage.css';

const HomePage = () => {
  return (
    <section className="home" id="home">
      <div className="home-content">
        <h1 className="home-title">  Welcome to De-LlMIT!!</h1>
        <p className="home-tagline">
          Decentralized Large LM Inference and Fine-Tuning. 
          Empowering AI with own edge device !!. 
        </p>
        <button className="cta-button">Explore Features   </button>
      </div>
    </section>
  );
};

export default HomePage;
