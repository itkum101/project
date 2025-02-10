import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './FeatureSection.css';

const FeaturesSection = () => {
  // State to store features fetched from the API
  const [features, setFeatures] = useState([]);

  // Fetch features from the backend on component mount
  useEffect(() => {
    const fetchFeatures = async () => {
      try {
        const response = await axios.get('http://backend-service:5000/features'); // Change URL if needed
        setFeatures(response.data); // Set the fetched features to state
      } catch (error) {
        console.error('Error fetching features:', error);
      }
    };

    fetchFeatures();
  }, []); // Empty dependency array ensures it runs only once on mount

  return (
    <section className="features" id="features">
      <h2 className="features-title">Key Features</h2>
      <div className="features-container">
        {features.length > 0 ? (
          features.map((feature) => (
            <div key={feature.id} className="feature-card">
              <div className="feature-icon">🌐</div> {/* You can replace this with a dynamic icon if needed */}
              <h3 className="feature-title">{feature.title}</h3>
              <p className="feature-description">{feature.description}</p>
            </div>
          ))
        ) : (
          <p>Loading features...</p>
        )}
      </div>
    </section>
  );
};

export default FeaturesSection;
