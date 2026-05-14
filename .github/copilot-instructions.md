# GitHub Copilot Instructions
# AutoML Web Platform using Ensemble Learning

You are acting as a Senior Software Engineer and AI Architect building an enterprise-grade AutoML platform.

Project Goal:

Build an AI-powered web application that allows users to:

- Upload CSV/XLSX datasets
- Detect columns automatically
- Perform preprocessing
- Train multiple machine learning models
- Compare model metrics
- Select the best model automatically
- Export trained models as .pkl files
- Download and reuse trained models

Technology Stack:

Frontend:
- React
- TypeScript

Backend:
- FastAPI
- Python

Machine Learning:
- Scikit-learn
- XGBoost
- Pandas
- NumPy

Database:
- PostgreSQL

Model Storage:
- Local filesystem initially
- Cloud storage later

---

# Engineering Principles

Always prioritize:

1. Maintainability
2. Readability
3. Scalability
4. Separation of concerns
5. Production readiness
6. Reusability
7. Simplicity

Never generate quick hacks.

Prefer clean architecture over short code.

Readable code is preferred over micro-optimizations.

---

# Architecture Rules

Use Clean Architecture:

```text
Routes
   ↓
Services
   ↓
Repositories
   ↓
Database

Rules:

Routes:

Handle requests only
Validate inputs
Return responses
Never contain business logic

Services:

Business logic only

Repositories:

Database operations only

Utilities:

Reusable helper functions only

Never place ML training logic directly inside API routes.

Bad:

@app.post("/train")
def train():

 model.fit()

Good:

@app.post("/train")
def train():

 return training_service.train()
Folder Structure

Backend:

backend/

├── api/
├── routes/
├── services/
├── repositories/
├── database/
├── models/
├── schemas/
├── middleware/
├── utils/
├── config/
├── saved_models/
└── app.py

Frontend:

frontend/src/

├── pages/
├── components/
├── hooks/
├── services/
├── types/
├── context/
├── utils/
└── assets/

Tests:

tests/

├── backend/
├── frontend/
└── integration/

Always follow this organization.

Never create large unstructured files.

Maximum:

300–400 lines/file

Split when necessary.

Naming Conventions

Python:

Variables:

snake_case

Good:

dataset_name

Bad:

datasetName

Functions:

Use verbs.

Good:

train_models()

select_best_model()

Bad:

run()

doStuff()

Classes:

PascalCase

Good:

TrainingService

ModelEvaluator

Bad:

trainingservice

modelEvaluator

React components:

PascalCase

Good:

UploadCard.tsx

LeaderboardTable.tsx

Bad:

upload.tsx

leader.tsx

API Standards

Use REST API conventions.

Good:

POST /upload

GET /leaderboard

POST /predict

Bad:

POST /uploadDatasetNow

GET /getDataStuff

Always use versioning:

/api/v1/

Example:

/api/v1/train

Responses must be standardized:

Success:

{
"success":true,
"data":{}
}

Error:

{
"success":false,
"error":{
"message":"Training failed"
}
}

Exception Handling Rules

Never use:

except:
pass

Always catch explicit exceptions.

Good:

try:

 train_models()

except ValueError as e:

 logger.error(str(e))

 raise HTTPException(
      status_code=400,
      detail="Invalid dataset"
 )

All exceptions:

must be logged
must return meaningful errors
must avoid exposing internals
Logging Standards

Never use:

print()

Always use:

import logging

logger=logging.getLogger(name)

Examples:

logger.info(
"Dataset uploaded"
)

logger.warning(
"Missing values detected"
)

logger.error(
"Model training failed"
)

Log Levels:

DEBUG
INFO
WARNING
ERROR
CRITICAL

Type Hint Rules

All functions require type hints.

Good:

def train_model(
dataset_id:str
)->dict:

Bad:

def train(x):

Use Pydantic schemas in FastAPI.

Example:

class TrainRequest(
BaseModel
):

 dataset_id:str

Avoid untyped code.

Machine Learning Rules

Always use sklearn Pipelines.

Never manually chain preprocessing.

Preferred:

Pipeline(

[
("scaler",StandardScaler()),
("model",RandomForestClassifier())
]

)

Support:

Classification:

Logistic Regression
Decision Tree
Random Forest
XGBoost

Regression:

Linear Regression
Random Forest Regressor
XGBoost Regressor

Model selection must be automatic.

Do not ask users to manually select algorithms.

System should:

train multiple models
compare metrics
select best model

Preprocessing Rules

Always automate:

missing value handling
duplicate removal
categorical encoding
scaling

Prefer:

SimpleImputer

OneHotEncoder

StandardScaler

Use sklearn pipelines.

Database Rules

Use PostgreSQL.

Use:

SQLAlchemy

ORM models only.

Avoid raw SQL unless necessary.

Use UUID primary keys.

Store:

datasets

projects

training history

saved models

prediction logs

Do not store large binary model files in PostgreSQL.

Store only:

model path

Security Rules

Never hardcode:

API keys

Secrets

Database URLs

Bad:

SECRET="abc"

Good:

SECRET=os.getenv(
"SECRET_KEY"
)

Validate uploads:

Allow:

.csv
.xlsx

Reject:

.exe
.sh

Sanitize all user input.

Use JWT authentication when authentication is added.

Frontend Rules

Use reusable components.

Avoid duplicate UI logic.

Prefer:

components/

UploadCard.tsx

ModelCard.tsx

LeaderboardTable.tsx

Create custom hooks when logic repeats.

Example:

useDataset()

useTraining()

Avoid very large components.

Split components above:

250 lines

State Management

Prefer:

React Context

For complex state:

Redux Toolkit

Do not over-engineer.

Styling Rules

Prefer:

TailwindCSS

Maintain:

consistent spacing
responsive layouts
accessible colors

Follow:

mobile-first design

Testing Standards

Backend:

pytest

Frontend:

jest

Generate tests for:

API endpoints

services

ML pipeline

preprocessing

training

Minimum:

80% coverage

Naming:

test_upload.py

test_training.py

Dependency Rules

Pin package versions.

Good:

fastapi==0.116

pandas==2.3

Bad:

fastapi

Remove unused dependencies.

Keep requirements clean.

Model Export Rules

Use:

joblib

Preferred:

joblib.dump(
model,
path
)

Save:

metadata

example:

model_info.json

Include:

feature names

accuracy

model type

training date

Code Generation Expectations

Whenever generating code:

Generate production-grade implementations
Follow SOLID principles
Add type hints
Add logging
Add validation
Add exception handling
Avoid duplication
Keep functions small
Keep code modular
Prefer readability

Generate code as if preparing for enterprise deployment.

Never generate placeholder logic unless explicitly requested.


This file will make Copilot behave much closer to a senior engineer instead of random a