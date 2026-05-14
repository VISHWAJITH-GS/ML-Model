🚀 AutoML Web Platform using Ensemble Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-Language-3178C6)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An intelligent AI-powered AutoML platform that allows users to upload datasets and automatically generate the best machine learning model using automated preprocessing, ensemble learning, model evaluation, and export capabilities.

---

# 📌 Project Overview

Building machine learning pipelines manually requires:

- Data cleaning
- Feature engineering
- Model selection
- Training
- Evaluation
- Model exporting

This platform automates the complete workflow.

Workflow:

```text
Upload Dataset
      ↓
Dataset Analysis
      ↓
Feature Selection
      ↓
Automatic Preprocessing
      ↓
Train Multiple Models
      ↓
Compare Metrics
      ↓
Select Best Model
      ↓
Export .pkl
      ↓
Download Model

The system automatically chooses the best performing model and allows users to download and reuse it.

✨ Features
Dataset Handling
Upload CSV datasets
Upload Excel datasets
Dataset preview
Column detection
Missing value detection
Automated Machine Learning
Automatic preprocessing
Feature scaling
Encoding categorical variables
Duplicate removal
Automatic Model Selection

Supports:

Classification:

Logistic Regression
Decision Tree
Random Forest
SVM
XGBoost

Regression:

Linear Regression
Random Forest Regressor
XGBoost Regressor
Ensemble Learning

Supports:

Bagging
Boosting
Random Forest
XGBoost
Model Comparison

Metrics:

Classification:

Accuracy
Precision
Recall
F1 Score

Regression:

MAE
RMSE
R² Score
Export
Download trained model as .pkl
Model metadata generation
🛠 Tech Stack
Frontend
React
TypeScript
TailwindCSS
Backend
FastAPI
Python
Machine Learning
Scikit-learn
Pandas
NumPy
XGBoost
Database
PostgreSQL
Model Storage
Local storage
Cloud storage (future)
📁 Folder Structure
project/

├── docs/
│   ├── PRD.md
│   ├── SRS.md
│   ├── ARCHITECTURE.md
│   ├── USER_STORIES.md
│   ├── API_SPEC.md
│   ├── DB_SCHEMA.md
│   ├── CODING_RULES.md
│   ├── TASKS.md
│   └── UI_GUIDELINES.md
│
├── frontend/
│
│   └── src/
│       ├── pages/
│       ├── components/
│       ├── hooks/
│       └── services/
│
├── backend/
│
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── utils/
│   └── saved_models/
│
├── tests/
│
├── datasets/
│
├── .github/
│
├── requirements.txt
│
└── README.md
⚙ Installation

Clone repository:

git clone https://github.com/your-username/automl-platform.git

Move into project:

cd automl-platform
🔧 Environment Setup

Create environment:

python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Install backend dependencies:

pip install -r requirements.txt

Install frontend dependencies:

cd frontend

npm install
🔑 Environment Variables

Create:

.env

Example:

DATABASE_URL=postgresql://user:password@localhost:5432/automl

SECRET_KEY=your_secret_key

MODEL_STORAGE_PATH=saved_models/

MAX_UPLOAD_SIZE=100
▶ Running Backend

Move to backend:

cd backend

Run FastAPI:

uvicorn app:app --reload

Backend:

http://localhost:8000

Swagger:

http://localhost:8000/docs
▶ Running Frontend

Move to frontend:

cd frontend

Start:

npm run dev

Frontend:

http://localhost:5173
API Overview
Method	Endpoint	Description
POST	/upload	Upload dataset
GET	/columns	Detect columns
POST	/preprocess	Preprocess data
POST	/train	Train models
GET	/leaderboard	Get rankings
GET	/download-model	Download model
POST	/predict	Predict values
📷 Screenshots
Upload Page
[Upload page screenshot here]
Dashboard
[Dashboard screenshot here]
Leaderboard
[Leaderboard screenshot here]
Model Comparison
[Charts screenshot here]
💻 Usage Example

Step 1:

Upload:

student_data.csv

Step 2:

Select:

Inputs:

Age
Salary
Experience

Target:

Purchased

Step 3:

Click:

Train Models

Result:

Best Model:
XGBoost

Accuracy:
97%

Step 4:

Download:

best_model.pkl
Example Using Downloaded Model
import joblib

model = joblib.load(
     "best_model.pkl"
)

prediction = model.predict(
    [[22,30000,2]]
)

print(prediction)
🔮 Future Improvements

Planned features:

Hyperparameter tuning
SHAP explainability
PDF report generation
User authentication
Cloud deployment
Project history
Model versioning
Real-time training queue
Docker support
Kubernetes deployment
🤝 Contribution Guidelines

Fork repository

Create feature branch:

git checkout -b feature/new-feature

Commit:

git commit -m "feat(upload): add csv upload"

Push:

git push origin feature/new-feature

Open Pull Request

Testing

Backend:

pytest

Frontend:

npm test
📄 License

MIT License

Copyright (c) 2026

Permission is hereby granted to use, modify, distribute and sell copies of this software.