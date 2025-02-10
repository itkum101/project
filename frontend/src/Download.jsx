import React from 'react';
import './Download.css';

const DownloadableResources = () => {
  const resources = [
    {
      id: 1,
      title: "Project Proposal ",
      description: "A detailed overview of De-LlMIT's architecture and methodologies.",
      file: "https://drive.google.com/file/d/1-_GcvR0zDccxKpxHAYqbR3Nsh5_UNrkZ/view?usp=sharing",
      // Replace with the actual file path or URL
    },
    {
      id: 2,
      title: "Mid Term Report",
      description: "Comprehensive insights into the implementation and results.",
      file: "https://drive.google.com/file/d/1ney-Ku9gu-BoOxkD0j8yBlQ3k6H_ae6I/view?usp=sharing", // Replace with the actual file path or URL
    }
  ];

  return (
    <section className="resources" id="resources">
      <h2 className="resources-title">Downloadable Resources</h2>
      <p className="resources-subtitle">
        Access key documents to learn more about De-LlMIT:
      </p>
      <div className="resources-container">
        {resources.map((resource) => (
          <div key={resource.id} className="resource-card">
            <h3 className="resource-title">{resource.title}</h3>
            <p className="resource-description">{resource.description}</p>
            <a
              href={resource.file}
              download
              className="resource-download-button"
            >
              Download
            </a>
          </div>
        ))}
      </div>
    </section>
  );
};

export default DownloadableResources;
