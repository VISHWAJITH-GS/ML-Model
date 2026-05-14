REST API Specification
AutoML Web Platform using FastAPI

API Version: v1.0
Protocol: REST
Data Format: JSON
Authentication: JWT (future scope)
Base URL:

http://localhost:8000/api/v1

Framework: FastAPI

API Overview

The backend supports:

Dataset upload
Column detection
Data preprocessing
Automatic model training
Model evaluation
Leaderboard generation
Model download
Prediction requests
Common Response Format
Success Response
{
    "success": true,
    "message": "Operation successful",
    "data": {}
}
Error Response
{
    "success": false,
    "error": {
        "code": "ERROR_CODE",
        "message": "Detailed message"
    }
}
1. Upload Dataset
Endpoint
POST /upload
Description

Uploads a CSV or Excel dataset and stores it for processing.

Request Type
multipart/form-data
Request Payload
Field	Type	Required	Description
file	File	Yes	CSV or Excel dataset
Validation Rules
File required
Allowed formats:
.csv
.xlsx
Maximum size:
100MB
Example Request
POST /upload
Content-Type: multipart/form-data

File:

student_dataset.csv
Success Response

Status:

200 OK
{
    "success": true,
    "message":"Dataset uploaded successfully",
    "data":{
        "dataset_id":"DS1001",
        "rows":500,
        "columns":12
    }
}
Error Responses
Invalid File Type
400 Bad Request
{
    "success":false,
    "error":{
        "code":"INVALID_FILE",
        "message":"Only CSV and XLSX supported"
    }
}
2. Get Columns
Endpoint
GET /columns
Description

Returns detected columns from uploaded dataset.

Query Parameters
Parameter	Required
dataset_id	Yes
Validation Rules
Dataset ID must exist
Example Request
GET /columns?dataset_id=DS1001
Success Response
{
"success":true,
"data":{

"columns":[
"Age",
"Salary",
"Experience",
"Purchased"
],

"numerical":[
"Age",
"Salary"
],

"categorical":[
"Purchased"
],

"missing_values":{
"Salary":5
}

}
}
Error Responses
404 Not Found
{
"success":false,
"error":{
"code":"DATASET_NOT_FOUND",
"message":"Dataset not found"
}
}
3. Preprocess Dataset
Endpoint
POST /preprocess
Description

Performs automatic preprocessing.

Operations:

missing value handling
encoding
scaling
duplicate removal
Request Payload
{
"dataset_id":"DS1001",

"input_columns":[
"Age",
"Salary",
"Experience"
],

"target_column":"Purchased"
}
Validation Rules
Dataset must exist
Target required
Input fields required
Success Response
{
"success":true,

"data":{

"duplicates_removed":15,

"missing_values_fixed":25,

"encoding":"completed",

"scaling":"completed"

}
}
Error Responses
400 Bad Request
{
"error":{
"message":"Target column required"
}
}
4. Train Models
Endpoint
POST /train
Description

Automatically trains multiple ML models and selects the best one.

Request Payload
{
"dataset_id":"DS1001"
}
Workflow

Backend:

preprocess data
train multiple models
evaluate
compare
select best
Success Response
{
"success":true,

"data":{

"problem_type":"classification",

"models_trained":[

"RandomForest",
"DecisionTree",
"XGBoost"

],

"best_model":"XGBoost",

"accuracy":0.97

}
}
Status Codes
Code	Meaning
200	Success
400	Validation Error
500	Training Failure
Error Response
{
"success":false,

"error":{

"code":"TRAINING_FAILED",

"message":"Unable to train models"

}
}
5. Get Leaderboard
Endpoint
GET /leaderboard
Description

Returns model comparison results.

Query Parameters
Parameter	Required
dataset_id	Yes
Example Request
GET /leaderboard?dataset_id=DS1001
Success Response
{
"success":true,

"data":[

{
"rank":1,
"model":"XGBoost",
"accuracy":0.97
},

{
"rank":2,
"model":"RandomForest",
"accuracy":0.95
},

{
"rank":3,
"model":"SVM",
"accuracy":0.91
}

]

}
Error Responses
404 Not Found
{
"error":{
"message":"No models found"
}
}
6. Download Model
Endpoint
GET /download-model
Description

Downloads generated model file.

Query Parameters
Parameter	Required
model_id	Yes
Example Request
GET /download-model?model_id=M1001
Success Response

Response type:

application/octet-stream

File:

best_model.pkl
Error Response
{
"success":false,

"error":{
"message":"Model not found"
}
}
7. Prediction API
Endpoint
POST /predict
Description

Uses saved trained model to generate predictions.

Request Payload
{
"model_id":"M1001",

"features":{

"Age":22,
"Salary":30000,
"Experience":2

}
}
Validation Rules
Model ID required
Feature count must match model metadata
Input values required
Success Response
{
"success":true,

"data":{

"prediction":"Yes"

}
}
Regression Example
{
"success":true,

"data":{

"prediction":45000

}
}
Error Response
{
"success":false,

"error":{

"code":"INVALID_INPUT",

"message":"Feature mismatch"

}
}
HTTP Status Codes
Code	Meaning
200	Success
201	Created
400	Bad Request
401	Unauthorized
404	Not Found
413	Payload Too Large
422	Validation Error
500	Internal Server Error
API Flow Diagram
User
  ↓

React Frontend

  ↓

POST /upload

  ↓

GET /columns

  ↓

POST /preprocess

  ↓

POST /train

  ↓

GET /leaderboard

  ↓

GET /download-model

  ↓

POST /predict
Future API Extensions

Planned endpoints:

POST /login
POST /register
GET /projects
GET /history
POST /reports
GET /saved-models
End of API Specification Document
