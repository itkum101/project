import React from 'react';
import './FutureSection.css';

const FutureWorkSection = () => {
  const futureWorks = [
    {
      id: 1,
      title: "Improve Browser-Based Inference",
      description:
        "Enhance the performance and compatibility of WebGPU-based inference across different devices and browsers.",
    },
  
    {
      id: 2,
      title: "Advanced Model Fine-Tuning",
      description:
        "Introduce fine-tuning capabilities for large language models to support a broader range of tasks.",
    },
    {
      id: 3,
      title: "Global Collaboration",
      description:
        "Create a user-friendly interface for participants to join the decentralized network and contribute resources.",
    },
  ];

  return (
    <section className="future-work" id="future-work">
      <h2 className="future-work-title">Future Work</h2>
      <p className="future-work-subtitle">
        Here are the next steps in the evolution of De-LlMIT:
      </p>
      <div className="future-work-container">
        {futureWorks.map((work) => (
          <div key={work.id} className="future-work-card">
            <h3 className="future-work-title">{work.title}</h3>
            <p className="future-work-description">{work.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default FutureWorkSection;
