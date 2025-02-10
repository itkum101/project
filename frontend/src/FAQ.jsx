import React, { useState } from 'react';
import './FAQ.css';

const FAQsSection = () => {
  const faqs = [
    {
      id: 1,
      question: "What is De-LlMIT?",
      answer:
        "De-LlMIT is a decentralized system for large language model inference and fine-tuning. It uses distributed computing to run AI models efficiently across multiple peers.",
    },
    {
      id: 2,
      question: "How does decentralized inference work?",
      answer:
        "Decentralized inference splits AI models into smaller shards and runs them on different devices, combining results in real-time. This reduces the need for expensive centralized hardware.",
    },
    {
      id: 3,
      question: "What technologies does De-LlMIT use?",
      answer:
        "De-LlMIT leverages WebGPU for browser-based inference, peer-to-peer networking for communication, and fault-tolerant architecture for scalability.",
    },
    {
      id: 4,
      question: "Can I contribute to De-LlMIT?",
      answer:
        "Yes! De-LlMIT is open for collaboration. You can contribute by running nodes, testing the system, or providing feedback.",
    },
  ];

  const [activeFAQ, setActiveFAQ] = useState(null);

  const toggleFAQ = (id) => {
    setActiveFAQ(activeFAQ === id ? null : id);
  };

  return (
    <section className="faqs" id="faqs">
      <h2 className="faqs-title">Frequently Asked Questions</h2>
      <div className="faqs-container">
        {faqs.map((faq) => (
          <div key={faq.id} className="faq-item">
            <div
              className={`faq-question ${activeFAQ === faq.id ? "active" : ""}`}
              onClick={() => toggleFAQ(faq.id)}
            >
              {faq.question}
            </div>
            {activeFAQ === faq.id && (
              <div className="faq-answer">{faq.answer}</div>
            )}
          </div>
        ))}
      </div>
    </section>
  );
};

export default FAQsSection;
