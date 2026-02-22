# MajorMatch – AI-Powered Academic Guidance System

🎯 **Purpose**  
MajorMatch is an AI-driven system that recommends suitable university majors based on a student's academic performance and interests.

🚀 **Why this project matters**
- Demonstrates end-to-end AI system design
- Combines Machine Learning, Backend APIs, and Modern Frontend
- Fully deployed with CI/CD on Render using GitLab

🔗 **Live Demo**
- 🌐 Frontend Dashboard: https://majormatch-frontend.onrender.com/
- 🛠️ API Documentation: https://majormatch-backend.onrender.com/docs

🧠 **Key Skills Demonstrated**
- Machine Learning (Scikit-learn, Random Forest)
- Backend Development (FastAPI, REST APIs)
- Frontend Development (React, Vite, modern UI)
- Deployment & CI/CD (GitLab + Render)

---

## Project Goal
MajorMatch helps students make informed academic decisions by analyzing academic scores and personal interests using a data-driven machine learning approach.

---

## Key Features
- **AI Predictions**: Random Forest Classifier for major recommendations
- **Modern UI**: Dark-themed Glassmorphism React interface
- **Decoupled Architecture**: Independent backend and frontend
- **Production Deployment**: Automated CI/CD with GitLab and Render

---

## Architecture Overview
- **Frontend**: React dashboard for user interaction
- **Backend**: FastAPI service exposing prediction APIs
- **ML Layer**: Trained Scikit-learn model loaded at runtime
- **Deployment**: Render with GitLab-based CI/CD

---

## Project Structure
```text
MajorMatch/
├── backend/
│   ├── app/
│   │   ├── api/             # FastAPI routes
│   │   ├── models/          # Pydantic schemas
│   │   ├── services/        # ML logic & PDF generation
│   │   └── main.py          # App entry & CORS setup
│   ├── data/                # student_data.csv
│   ├── ml_models/           # Serialized ML models (.pkl)
│   ├── scripts/             # Model training scripts
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── services/        # API abstraction layer
│   │   ├── App.jsx          # UI logic
│   │   └── App.css          # Glassmorphism styles
│   ├── package.json
│   └── vite.config.js
├── .gitignore
└── README.md
```

---

## Tech Stack

**Frontend**
- React 19
- Vite 7
- CSS3 (Glassmorphism / Bento layout)

**Backend**
- Python 3.x
- FastAPI
- Uvicorn
- ReportLab (PDF generation)

**Machine Learning**
- Scikit-learn (Random Forest)
- Pandas

**Environment**
- Node.js 22+
- Python Virtual Environments

---

## Running the Project Locally

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Train the model
python scripts/train_model.py

# Start API server
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## Model Insights
- **Predictive Focus**: Math and Physics scores are weighted heavily for STEM-related recommendations.
- **Encoding Strategy**: Categorical interests are transformed using LabelEncoders to ensure ML compatibility.

---

## Evaluation Notes
This project highlights:
- Full-stack AI application development
- Clean separation of concerns
- Production deployment experience
- Practical application of machine learning models
# MajorMatch
