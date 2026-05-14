Software Architecture Document
AutoML Web Platform using Ensemble Learning

Document Version: 1.0
Architecture Type: Web-Based AI/ML Platform
Project: AutoML Web Platform using Ensemble Learning
Status: Draft
Date: May 2026

1. Introduction
1.1 Overview

The AutoML Web Platform is a web-based AI system that automates machine learning model generation from uploaded datasets. Users upload datasets, define input/output columns, and the system automatically preprocesses data, trains multiple models, evaluates them, selects the best model, and exports the trained model as a .pkl file.

The platform follows a modular architecture using:

Frontend: React
Backend: FastAPI
Machine Learning: Scikit-learn, XGBoost
Database: PostgreSQL
Model Storage: Local filesystem / Cloud storage
2. High-Level Architecture

The system follows a multi-layer architecture:

+-------------------+
|   User Browser    |
+-------------------+
          |
          v
+-------------------+
| React Frontend    |
+-------------------+
          |
 REST API Calls
          |
          v
+-------------------+
| FastAPI Backend   |
+-------------------+
      |        |
      |        |
      |        +----------------------+
      |                               |
      v                               v
+-------------+             +------------------+
| ML Engine   |             | PostgreSQL DB    |
| ScikitLearn |             | Metadata Storage |
| XGBoost     |             +------------------+
+-------------+
      |
      |
      v
+----------------------+
| Model Storage        |
| Local / Cloud (.pkl) |
+----------------------+
3. System Components

The architecture contains the following modules:

Component	Responsibility
React Frontend	UI and user interaction
FastAPI Backend	API management
Upload Service	Dataset processing
Preprocessing Service	Data cleaning
Training Engine	Model generation
Evaluation Engine	Performance comparison
Model Selector	Best model selection
Storage Service	Model saving
Database	Metadata storage
4. Frontend Architecture

Frontend uses React component-based architecture.

Responsibilities:

Dataset upload
Feature selection
Visualization
Progress display
Model leaderboard
Download trained model
Frontend Structure
src/
│
├── pages/
│   ├── Home
│   ├── Upload
│   ├── Dashboard
│   ├── Leaderboard
│
├── components/
│   ├── UploadCard
│   ├── DataPreview
│   ├── Charts
│   ├── ModelTable
│
├── services/
│   ├── api.js
│
├── hooks/
│
├── utils/
│
└── App.js
5. Backend Architecture

FastAPI handles:

API endpoints
business logic
training orchestration
model persistence

Architecture follows layered structure:

API Layer
      ↓
Service Layer
      ↓
ML Processing Layer
      ↓
Storage Layer
Backend Structure
backend/
│
├── api/
│
├── routes/
│
├── services/
│   ├── upload_service.py
│   ├── preprocess_service.py
│   ├── training_service.py
│   ├── evaluation_service.py
│
├── models/
│
├── database/
│
├── utils/
│
└── app.py
6. ML Pipeline Architecture

The ML engine forms the core intelligence of the system.

Pipeline stages:

Data Loading
Data Cleaning
Missing Value Handling
Feature Encoding
Scaling
Train-Test Split
Multiple Model Training
Model Evaluation
Best Model Selection
Export Model
ML Pipeline Flow
Dataset
   ↓
Data Cleaning
   ↓
Missing Value Handler
   ↓
Encoding
   ↓
Scaling
   ↓
Split Data
   ↓
Train Models
   ↓
Evaluate
   ↓
Select Best Model
   ↓
Save PKL
7. Request-Response Flow

The frontend communicates with backend using REST APIs.

Upload Dataset Flow
User
   ↓
React Upload Page
   ↓
POST /upload
   ↓
FastAPI
   ↓
Read Dataset
   ↓
Store Metadata
   ↓
Return Dataset Info
Model Training Flow
User
   ↓
POST /train
   ↓
FastAPI
   ↓
Preprocessing
   ↓
ML Training Engine
   ↓
Evaluation
   ↓
Best Model
   ↓
Save PKL
   ↓
Return Results
8. Data Flow Diagram
Level 0 DFD
        +----------------+
        |     User       |
        +--------+-------+
                 |
                 |
                 v
+--------------------------------+
| AutoML Web Platform            |
+--------------------------------+
       |               |
       |               |
       v               v

Dataset          Model Results
Upload            Download
Level 1 DFD
User
   |
   v
Upload Dataset
   |
   v
Read Dataset
   |
   v
Preprocessing
   |
   v
Model Training
   |
   v
Evaluation
   |
   v
Leaderboard
   |
   v
Best Model Export
9. Component Interaction Diagram
User
 ↓

React Frontend

 ↓

FastAPI API

 ↓

Upload Service

 ↓

Preprocessing Service

 ↓

Training Engine

 ↓

Evaluation Service

 ↓

Model Selector

 ↓

Model Storage
10. Recommended Folder Structure
project/
│
├── frontend/
│
│   ├── src/
│   │
│   ├── pages/
│   ├── components/
│   ├── hooks/
│   └── services/
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
├── docs/
│
├── tests/
│
├── datasets/
│
├── requirements.txt
│
└── README.md
11. Deployment Architecture

Production deployment:

                    User
                      |
                      v

            +----------------+
            | React Frontend |
            +----------------+
                     |
                     v

             API Gateway
                     |
                     v

            +----------------+
            | FastAPI Server |
            +----------------+
                |        |
                |        |
                |        |
                v        v

        PostgreSQL   ML Service

                     |
                     v

              Model Storage
12. Scalability Considerations
Horizontal Scaling

Backend instances can scale using:

Docker
Kubernetes
Asynchronous Training

Long model training should use:

Background workers
Task queues

Example:

FastAPI
   ↓
Task Queue
   ↓
ML Worker
Caching

Add:

Redis cache

Use for:

repeated predictions
model metadata
Future Enhancements

Support:

cloud storage
distributed training
GPU processing
13. Security Architecture
File Validation Layer

Validate:

extension
size
structure

Allowed:

.csv
.xlsx
API Security

Use:

JWT Authentication
Role-based authorization
Data Protection

Protect:

uploaded datasets
generated models
logs
Security Flow
User Request
      ↓
Authentication
      ↓
Authorization
      ↓
Input Validation
      ↓
API Processing
      ↓
Response
Secure Model Download

Before model download:

Validate:

user identity
project ownership
14. End-to-End Workflow
Dataset Upload
        ↓
Dataset Analysis
        ↓
Column Detection
        ↓
Input/Output Selection
        ↓
Automatic Preprocessing
        ↓
Train Multiple Models
        ↓
Model Evaluation
        ↓
Leaderboard Generation
        ↓
Best Model Selection
        ↓
Export PKL
        ↓
Download Model
Architecture Principles

The architecture follows:

Modular design
Separation of concerns
Service-oriented structure
Clean architecture
Scalability-first approach
API-driven communication
Maintainability
End of Architecture Document