Coding Standards and Engineering Rules
AutoML Web Platform using Ensemble Learning

Version: 1.0
Project Type: AI/ML Web Platform
Technology Stack: Python, FastAPI, React, TypeScript, Scikit-learn
Architecture Style: Clean Architecture + Service Layer Pattern
Status: Engineering Standard Document

1. Purpose

This document defines engineering standards and coding conventions for the AutoML platform.

Objectives:

Maintain consistency
Improve readability
Reduce technical debt
Increase maintainability
Enforce scalable architecture
Support collaboration

All developers and AI coding assistants must follow these rules.

2. Naming Conventions
Python Variables
Rule

Use:

snake_case
Good
dataset_name = "students.csv"

model_accuracy = 0.95
Bad
datasetName="students.csv"

ModelAccuracy=0.95
Functions

Use descriptive verbs.

Good
load_dataset()

train_models()

select_best_model()
Bad
doStuff()

run()

abc()
Classes

Use:

PascalCase
Good
ModelTrainer

DatasetService
Bad
modeltrainer

dataset_service
React Components

Use:

PascalCase
Good
UploadCard.tsx

ModelLeaderboard.tsx
Bad
uploadcard.tsx

leader.tsx
Constants

Use:

MAX_UPLOAD_SIZE=100

Not:

maxUploadSize=100
3. Folder Structure Rules

Project structure:

project/

├── frontend/
│
├── backend/
│
├── docs/
│
├── tests/
│
├── datasets/
│
└── README.md
Backend Structure
backend/

├── api/
├── routes/
├── services/
├── repositories/
├── models/
├── schemas/
├── utils/
├── database/
├── middleware/
├── config/
└── saved_models/
Frontend Structure
frontend/

src/

├── pages/
├── components/
├── services/
├── hooks/
├── context/
├── utils/
├── assets/
└── types/
Rule

Business logic must never exist inside route files.

Good
routes
   ↓
service
   ↓
repository
Bad
@app.post("/train")

def train():

    entire_logic_here()
4. API Design Rules
Use REST naming conventions
Good
POST /upload

GET /leaderboard

POST /predict
Bad
POST /uploadDataNow

GET /getLeaderboardData
Use versioning

Good:

/api/v1/train

Bad:

/autoTrainModel
Return standardized responses

Good:

{
"success":true,
"data":{}
}

Bad:

{
"ok":"yes"
}
5. Function Structure Rules

Function responsibilities:

One purpose
Small size
Reusable

Maximum:

30–40 lines
Good
def preprocess_dataset():

     clean_data()

     encode_features()

     scale_features()
Bad
def process():

   #500 lines
6. Exception Handling Rules

Never use:

except:
      pass
Good
try:

     train_model()

except ValueError as e:

     logger.error(str(e))

     raise HTTPException(
          status_code=400,
          detail="Training failed"
     )
Bad
try:

   train()

except:

   print("error")
Rule

Always:

catch specific exceptions
log errors
return user-friendly messages
7. Logging Standards

Use:

logging

Never:

print()
Good
logger.info(
     "Dataset uploaded"
)

logger.error(
     "Training failed"
)
Bad
print("working")

Log levels:

Level	Usage
DEBUG	Development
INFO	System actions
WARNING	Unexpected events
ERROR	Failures
CRITICAL	System crashes
8. Security Practices
Never commit secrets

Forbidden:

SECRET="abcd123"

Correct:

SECRET=os.getenv(
     "SECRET_KEY"
)
Validate uploads

Allowed:

.csv
.xlsx

Reject:

.exe
.sh
Sanitize input

Always validate:

request data
query params
file uploads
Passwords

Use:

bcrypt

Never:

plain text
9. Type Hint Rules

All functions require type hints.

Good
def train_model(
     dataset_id:str
)->dict:
Bad
def train_model(x):
React TypeScript

Good:

interface DatasetProps{

     id:string

     name:string
}

Bad:

const data:any

Avoid:

any
10. Documentation Standards

Every module requires:

purpose
parameters
return values
Good
def preprocess_data(
      df:DataFrame
)->DataFrame:

   """
   Clean and preprocess dataset

   Args:

      df:input dataframe

   Returns:

      cleaned dataframe
   """

Bad:

def clean(df):
11. Git Commit Conventions

Use:

type(scope): message

Examples:

feat(upload): add csv upload endpoint

fix(training): solve xgboost issue

docs(api): update api specs

refactor(service): improve model selection

Allowed prefixes:

feat
fix
docs
style
refactor
test
chore

Bad:

final

working code

update
12. Environment Variable Rules

Use:

.env

Never:

Hardcode values.

Good:

DATABASE_URL=

SECRET_KEY=

API_KEY=

Load using:

from dotenv import load_dotenv

Add:

.env.example

Git ignore:

.env
13. Testing Standards

Frameworks:

Backend:

pytest

Frontend:

jest

Naming:

test_upload.py

test_training.py

Structure:

def test_upload_success():

def test_upload_failure():

Minimum coverage:

80%

Test:

APIs
services
preprocessing
training
14. Dependency Management

Use:

requirements.txt

or

poetry

Pin versions.

Good:

fastapi==0.116.0

pandas==2.3.0

Bad:

fastapi

Update:

Monthly

Remove:

Unused packages

15. Clean Architecture Principles

Architecture:

Routes
   ↓

Services
   ↓

Repositories
   ↓

Database

Rules:

Routes

Only:

request validation
response formatting
Services

Contains:

business logic

Repository

Handles:

database operations

Utilities

Reusable helpers only

Good Example
route
   ↓

training_service
   ↓

model_repository
Bad Example
route

↓

database query

↓

training logic

↓

response formatting

Everything inside one file.

16. File Organization Rules

One file = one responsibility

Good:

preprocessing_service.py

evaluation_service.py

training_service.py

Bad:

all_services.py

Maximum:

300–400 lines/file

Split if larger.

17. Best Practices Summary

✅ Modular code

✅ Reusable services

✅ Type hints everywhere

✅ Logging instead of print

✅ Small functions

✅ REST APIs

✅ Secure uploads

✅ Unit tests

✅ Versioned APIs

✅ Environment variables

✅ Clean architecture

✅ Standard naming conventions

End of Engineering Rules Document