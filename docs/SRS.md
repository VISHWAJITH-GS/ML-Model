Software Requirements Specification (SRS)
AutoML Web Platform using Ensemble Learning

Document Version: 1.0
Document Type: Software Requirements Specification (SRS)
Standard: IEEE SRS Format
Project Name: AutoML Web Platform using Ensemble Learning
Prepared By: Software Engineering Team
Date: May 2026
Status: Draft

1. Introduction
1.1 Overview

The AutoML Web Platform is an AI-powered web application that automates the machine learning workflow for structured datasets. Users upload datasets and the platform automatically preprocesses data, trains multiple machine learning models, compares performance metrics, selects the best model, and exports the trained model as a downloadable .pkl file.

The system is designed to reduce manual effort and simplify machine learning for users with varying levels of expertise.

1.2 Document Purpose

This Software Requirements Specification (SRS) document defines the complete functional and non-functional requirements for the AutoML platform.

The purpose of this document is to:

Establish project scope
Define system behavior
Specify requirements
Provide implementation guidance
Serve as a reference throughout development
1.3 Intended Audience

This document is intended for:

Software developers
ML engineers
Project managers
QA engineers
Stakeholders
Researchers
Students
2. Purpose of the System

The system aims to automate machine learning model generation and reduce the need for users to manually:

preprocess datasets
select algorithms
train models
compare results
export trained models

The system automatically performs these tasks and recommends the best model based on evaluation metrics.

3. Scope

The application shall provide:

Dataset Handling
Upload CSV datasets
Upload Excel datasets
Dataset preview
Data Processing
Detect numerical columns
Detect categorical columns
Detect missing values
Machine Learning Pipeline
Automatic preprocessing
Model training
Ensemble learning
Model comparison
Best model selection
Output Features
Leaderboard generation
Model download
Export .pkl file
Excluded Scope (Version 1)

The following are not included:

Image datasets
NLP datasets
Deep learning models
Distributed computing
Real-time streaming data
4. Definitions and Abbreviations
Term	Description
AI	Artificial Intelligence
ML	Machine Learning
AutoML	Automated Machine Learning
API	Application Programming Interface
UI	User Interface
CSV	Comma Separated Values
X	Input features
Y	Target feature
PKL	Serialized machine learning model file
MAE	Mean Absolute Error
RMSE	Root Mean Square Error
F1	F1 Score
5. System Overview

The system consists of:

Frontend

Technology:

React

Responsibilities:

User interaction
Dataset upload
Visualization
Display metrics
Backend

Technology:

FastAPI

Responsibilities:

API handling
preprocessing
model orchestration
Machine Learning Layer

Libraries:

Scikit-learn
Pandas
XGBoost

Responsibilities:

preprocessing
training
evaluation
export
System Workflow
User Uploads Dataset
        ↓
Read Dataset
        ↓
Detect Features
        ↓
Select X and Y
        ↓
Automatic Preprocessing
        ↓
Train Multiple Models
        ↓
Compare Results
        ↓
Select Best Model
        ↓
Generate PKL
        ↓
Download Model
6. User Roles
Role 1: Guest User

Permissions:

Upload datasets
Train models
Download model files
Role 2: Registered User

Permissions:

Access previous projects
View model history
Save datasets
Role 3: Administrator

Permissions:

Monitor system
Manage users
View logs
7. Functional Requirements
REQ-001

System shall allow users to upload CSV datasets.

Priority:
High

REQ-002

System shall allow Excel file upload.

Priority:
High

REQ-003

System shall preview uploaded datasets.

Priority:
High

REQ-004

System shall detect missing values.

Priority:
High

REQ-005

System shall classify columns into:

numerical
categorical

Priority:
High

REQ-006

System shall allow users to select input features.

Priority:
High

REQ-007

System shall allow users to select target feature.

Priority:
High

REQ-008

System shall preprocess datasets automatically.

Includes:

imputation
encoding
scaling

Priority:
High

REQ-009

System shall automatically train multiple ML models.

Priority:
High

REQ-010

System shall support:

Classification:

Logistic Regression
Decision Tree
Random Forest
XGBoost

Regression:

Linear Regression
Random Forest Regressor
XGBoost Regressor

Priority:
High

REQ-011

System shall compare trained model metrics.

Priority:
High

REQ-012

System shall generate model leaderboard.

Priority:
Medium

REQ-013

System shall automatically select the best model.

Priority:
High

REQ-014

System shall export trained model as .pkl.

Priority:
High

REQ-015

System shall allow model download.

Priority:
High

8. Non-Functional Requirements
REQ-NF-001

System response time shall remain under:

5 seconds for upload operations.

REQ-NF-002

Model generation should complete within:

60 seconds for medium datasets.

REQ-NF-003

UI shall support responsive layouts.

REQ-NF-004

System shall maintain 99% availability.

REQ-NF-005

System shall provide clear error messages.

9. Security Requirements
REQ-SEC-001

System shall validate uploaded file types.

Allowed:

CSV
XLSX
REQ-SEC-002

System shall restrict executable uploads.

REQ-SEC-003

System shall sanitize user input.

REQ-SEC-004

System shall prevent injection attacks.

REQ-SEC-005

System shall use HTTPS in production.

REQ-SEC-006

System shall log suspicious activity.

10. Performance Requirements
REQ-PER-001

Dataset upload:

<5 seconds

REQ-PER-002

Dataset analysis:

<10 seconds

REQ-PER-003

Model training:

<60 seconds

REQ-PER-004

Support concurrent requests:

100 users

11. Scalability Requirements
REQ-SCAL-001

System shall support horizontal scaling.

REQ-SCAL-002

Support future cloud deployment.

REQ-SCAL-003

Allow asynchronous training jobs.

REQ-SCAL-004

Support future distributed processing.

12. Error Handling Requirements
REQ-ERR-001

Invalid file uploads must display:

"Unsupported file format."

REQ-ERR-002

Empty datasets shall produce:

"Dataset contains no records."

REQ-ERR-003

Missing target selection:

"Please select target column."

REQ-ERR-004

Training failures shall display:

"Model generation failed."

REQ-ERR-005

All backend exceptions shall be logged.

13. Constraints
Technical Constraints

Frontend:

React

Backend:

FastAPI

ML:

Scikit-learn
XGBoost
Pandas
Infrastructure Constraints
Limited server memory
Limited CPU resources
Dataset Constraints

Version 1 supports:

Structured tabular datasets only
File Constraints

Maximum upload size:

100 MB

14. Future Enhancements
Hyperparameter Tuning

Use:

GridSearchCV
RandomSearchCV
Explainable AI

Add:

SHAP
Feature importance
Cloud Model Deployment

Support:

deployment APIs
User Authentication

Features:

login
saved projects
Report Generation

Generate:

PDF reports
charts
confusion matrix reports
AI Recommendation System

Example:

Random Forest is recommended for this dataset.

Appendix A: Technology Stack
Layer	Technology
Frontend	React
Backend	FastAPI
ML	Scikit-learn
Data	Pandas
ML Models	XGBoost
Serialization	Joblib / Pickle
Appendix B: Assumptions
Users upload clean tabular datasets
Datasets contain target variables
Internet access exists during use
Users understand basic prediction concepts
End of Document
