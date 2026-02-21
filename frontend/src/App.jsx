import { useState } from 'react';
import { predictMajor } from './services/api';
import './App.css';

export default function App() {
  const [formData, setFormData] = useState({ math: 50, physics: 50, chemistry: 50, english: 50, interest: 'Science' });
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const data = await predictMajor(formData);
    setPrediction(data.major);
    setLoading(false);
  };

  return (
    <div className="main-wrapper">
      <div className="major-card">
        <header className="card-header">
          <h1>Major AI Guide</h1>
          <p>Full-Stack Recommendation Engine</p>
        </header>

        <form onSubmit={handleSubmit}>
          <div className="input-grid">
            {['math', 'physics', 'chemistry', 'english'].map((subject) => (
              <div key={subject} className="input-group">
                <label>{subject.toUpperCase()}</label>
                <input 
                  type="number" 
                  value={formData[subject]}
                  onChange={(e) => setFormData({...formData, [subject]: e.target.value})} 
                />
              </div>
            ))}
          </div>

          <div className="input-group full-width">
            <label>CORE INTEREST</label>
            <select value={formData.interest} onChange={(e) => setFormData({...formData, interest: e.target.value})}>
              <option value="Science">Science</option>
              <option value="Technology">Technology</option>
              <option value="Engineering">Engineering</option>
              <option value="Arts">Arts</option>
            </select>
          </div>

          <button type="submit" className="analyze-btn">
            {loading ? 'Analyzing...' : 'Analyze My Future'}
          </button>
        </form>

        {prediction && (
          <div className="result-section">
            <div className="result-box path">
              <span className="label">RECOMMENDED PATH</span>
              <span className="value green">{prediction}</span>
            </div>
            <div className="result-box confidence">
              <span className="label">ML CONFIDENCE</span>
              <span className="value">High Match</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}