# MajorMatch: AI-Driven Academic Guidance

## Project Goal
MajorMatch is an end-to-end recommendation engine that analyzes student performance and interests to suggest the most suitable university major. It features a high-performance FastAPI backend, a machine learning brain powered by Scikit-learn, and a modern React frontend with Glassmorphism styling.

## Project Structure
The project is decoupled into a stateful AI backend and a modern React dashboard.

MajorMatch/
├── backend/
│   ├── app/
│   │   ├── api/             # API routes (FastAPI)
│   │   ├── models/          # Pydantic data schemas
│   │   ├── services/        # ML Logic & PDF Generation
│   │   └── main.py          # Entry point & CORS setup
│   ├── data/                # student_data.csv
│   ├── ml_models/           # Serialized .pkl files
│   ├── scripts/             # train_model.py
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── services/        # Modular API fetch logic
│   │   ├── App.jsx          # UI & State Logic
│   │   └── App.css          # Glassmorphism & Bento styles
│   ├── package.json         # Node dependencies
│   └── vite.config.js       # Vite configuration
├── .gitignore               # Multi-layer git exclusion
└── README.md

## Tools & Technologies

Frontend: React 19, Vite 7, CSS3 (Bento-box Layout).

Backend: Python 3.x, FastAPI, Uvicorn, ReportLab (PDF).

Machine Learning: Scikit-learn (Random Forest), Pandas.

Environment: Node.js 22+, Python Virtual Environments.


## Features

* **AI Predictions**: Uses a Random Forest Classifier to analyze student profiles.
* **Modern UI**: Sleek, dark-themed Glassmorphism interface built with React.
* **Automated CI/CD**: Integrated with GitLab CI and Render for seamless deployment.

## Running the Project

# Backend
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Step 1: Train the model
python scripts/train_model.py

# Step 2: Start the API
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev

## Model Insights
Predictive Power: Math and Physics scores are prioritized for STEM track recommendations.

Encoding: Categorical interests are transformed via LabelEncoders to ensure compatibility with the ML model
