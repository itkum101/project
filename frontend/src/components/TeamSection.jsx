import React from 'react';
import './TeamSection.css';

const TeamSection = () => {
  const teamMembers = [
    {
      id: 1,
      name: "Aavash Chhetri",
      role: "Developer",
      description: "Specializes in distributed systems and decentralized architecture",
      photo: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThm_sNap5JDlWIBTFj4sfaTiP7c1SoAC41M5KRZ57yS6oFRHIc_kgugzTb-uRvF1o_5lw",
    },
    {
      id: 2,
      name: "Kushal Poudel",
      role: "Developer",
      description: "Specializes in distributed systems and decentralized architecture",
      photo: "https://img.freepik.com/free-vector/young-prince-vector-illustration_1308-174367.jpg",
    },
    {
      id: 3,
      name: "Mukti Subedi",
      role: "Developer",
      description: "Specializes in distributed systems and decentralized architecture",
      photo: "https://img.freepik.com/free-vector/smiling-young-man-illustration_1308-174669.jpg",
    }
  ];

  return (
    <section className="team" id="team">
      <h2 className="team-title">Meet the Team</h2>
      <div className="team-container">
        {teamMembers.map((member) => (
          <div key={member.id} className="team-card">
            <img src={member.photo} alt={member.name} className="team-photo" />
            <h3 className="team-name">{member.name}</h3>
            <p className="team-role">{member.role}</p>
            <p className="team-description">{member.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default TeamSection;
