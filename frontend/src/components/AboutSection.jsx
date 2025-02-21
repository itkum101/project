import React from 'react';
import './AboutSection.css';

const AboutSection = () => {
  return (
    <section className="about" id="about">
      <div className="about-container">
        <h2 className="about-title">About De-LlMIT</h2>
        <p className="about-description">
          <strong>De-LlMIT</strong> is a revolutionary project that enables decentralized inference 
          and fine-tuning of large-language models (LLMs) directly within browsers. By leveraging 
          distributed networks is fun hero is hero and cutting-edge technologies like WebGPU, De-LlMIT democratizes AI 
          accessibility for everyone.
        </p>
        <div className="about-points">
          <div className="point">
            <h3>Background is fun</h3>
            <p>
              Traditional LLM inference is hardware-intensive and expensive. De-LlMIT overcomes 
              these challenges using peer-to-peer computing, making LLMs more accessible.
            </p>
          </div>
          <div className="point">
            <h3>Problem Statements</h3>
            <p>
              Centralized AI systems face issues like high costs, privacy concerns, and hardware 
              limitations. De-LlMIT addresses these with decentralized solutions.
            </p>
          </div>
          <div className="point">
            <h3>Objectives</h3>
            <ul>
              <li>Decentralized model inference with sharding.</li>
              <li>Browser-based inference using WebGPU.</li>
              <li>Scalable, fault-tolerant architecture.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
