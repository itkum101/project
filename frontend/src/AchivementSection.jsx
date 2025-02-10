import React from 'react';
import './AchivementSection.css';

const AchievementsSection = () => {
    const achievements = [
        {
          id: 1,
          title: "Model Sharding Implementation",
          description:
            "Successfully split large language models into smaller chunks for decentralized inference.",
          date: "March 2024",
        },
        {
            id: 2,
            title: "DHT and Logits Sharing",
            description: "Implemented decentralized model training and logits sharing using Hivemind's DHT with fault tolerance and peer communication.",
            date: "March 2024",
          },
          {
            id: 3,
            title: "NAT Traversal Implementation",
            description: "Enable seamless communication between peers behind different network configurations for better scalability",
            date: "March 2024",
          },
          {
            id: 4,
            title: "Testing on Kaggle and Google Colab",
            description: "Successfully tested decentralized model training and logits sharing on Kaggle and Google Colab.",
            date: "March 2024",
          }
      ];

  return (
    <section className="achievements" id="achievements">
      <h2 className="achievements-title">Our Achievements</h2>
      <p className="achievements-subtitle">
        Here are the milestones we’ve reached on our journey to democratize AI:
      </p>
      <div className="achievements-container">
        {achievements.map((achievement) => (
          <div key={achievement.id} className="achievement-card">
            <h3 className="achievement-title">{achievement.title}</h3>
            <p className="achievement-description">{achievement.description}</p>
            <p className="achievement-date">{achievement.date}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default AchievementsSection;
