import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import HomePage from './components/HomePage';
import AboutSection from './components/AboutSection';
import FeaturesSection from './components/FeatureSection';
import TeamSection from './components/TeamSection';
import AchievementsSection from './AchivementSection';
import FutureWorkSection from './FutureSection';
import FooterSection from './FooterSection';
import DownloadableResources from './Download';
import FAQsSection from './FAQ';
import InferenceDisplay from './InferenceDisplay';

function App() {
  return (
    <Router>
  
      <Routes>
        <Route path="/" element={
          <>
              <Header />
            <HomePage />
            <AboutSection />
            <FeaturesSection />
            <TeamSection />
            <AchievementsSection />
            <FutureWorkSection />
            <DownloadableResources />
            <FAQsSection />
            <FooterSection />
                      </>
        } />
        <Route path="/inference" element={<InferenceDisplay />} />
      </Routes>
    </Router>
  );
}

export default App;
