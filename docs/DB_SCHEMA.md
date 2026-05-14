Database Schema Design Document
AutoML Web Platform using Ensemble Learning

Database: PostgreSQL
Version: 1.0
Database Type: Relational Database
Architecture: Scalable Multi-user Design
Status: Draft

1. Database Overview

The AutoML platform requires persistent storage for:

User accounts
Projects
Uploaded datasets
Model training sessions
Evaluation results
Saved models
Prediction history

The database is designed for:

scalability
maintainability
analytics support
future SaaS expansion
2. Entity Relationship Overview

Core workflow:

User
 ↓
Projects
 ↓
Datasets
 ↓
Model Training
 ↓
Leaderboard
 ↓
Saved Models
 ↓
Prediction Logs
3. Table: users

Stores user account information.

Table Name
users
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Unique user ID
full_name	VARCHAR(100)	NOT NULL	—	User full name
email	VARCHAR(255)	UNIQUE, NOT NULL	—	User email
password_hash	TEXT	NOT NULL	—	Encrypted password
role	VARCHAR(20)	NOT NULL	'user'	user/admin
is_active	BOOLEAN	NOT NULL	TRUE	Account status
created_at	TIMESTAMP	NOT NULL	NOW()	Account creation
updated_at	TIMESTAMP	NOT NULL	NOW()	Last update
Primary Key
PRIMARY KEY(id)
Constraints
UNIQUE(email)
4. Table: projects

Stores project sessions.

Table Name
projects
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Project ID
user_id	UUID	FK	—	Project owner
project_name	VARCHAR(150)	NOT NULL	—	Project name
description	TEXT	NULL	—	Description
created_at	TIMESTAMP	NOT NULL	NOW()	Creation date
Foreign Keys
FOREIGN KEY(user_id)
REFERENCES users(id)
ON DELETE CASCADE
5. Table: datasets

Stores uploaded datasets.

Table Name
datasets
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Dataset ID
project_id	UUID	FK	—	Related project
file_name	VARCHAR(255)	NOT NULL	—	Original filename
file_type	VARCHAR(20)	NOT NULL	—	CSV/XLSX
file_size	BIGINT	NOT NULL	—	Size bytes
total_rows	INTEGER	NULL	—	Dataset rows
total_columns	INTEGER	NULL	—	Dataset columns
uploaded_at	TIMESTAMP	NOT NULL	NOW()	Upload timestamp
Foreign Keys
FOREIGN KEY(project_id)
REFERENCES projects(id)
ON DELETE CASCADE
6. Table: model_training

Stores model training sessions.

Table Name
model_training
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Training ID
dataset_id	UUID	FK	—	Dataset used
problem_type	VARCHAR(50)	NOT NULL	—	Classification/Regression
selected_features	JSONB	NOT NULL	'{}'	Feature list
target_column	VARCHAR(100)	NOT NULL	—	Prediction target
preprocessing_steps	JSONB	NULL	'{}'	Applied preprocessing
started_at	TIMESTAMP	NOT NULL	NOW()	Start time
completed_at	TIMESTAMP	NULL	—	End time
status	VARCHAR(20)	NOT NULL	'processing'	processing/completed/failed
Foreign Keys
FOREIGN KEY(dataset_id)
REFERENCES datasets(id)
7. Table: leaderboard

Stores model comparison scores.

Table Name
leaderboard
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Record ID
training_id	UUID	FK	—	Training session
model_name	VARCHAR(100)	NOT NULL	—	Model name
accuracy	NUMERIC(5,4)	NULL	—	Classification accuracy
precision_score	NUMERIC(5,4)	NULL	—	Precision
recall_score	NUMERIC(5,4)	NULL	—	Recall
f1_score	NUMERIC(5,4)	NULL	—	F1
rmse	NUMERIC(10,4)	NULL	—	Regression RMSE
rank	INTEGER	NOT NULL	—	Ranking
Foreign Keys
FOREIGN KEY(training_id)
REFERENCES model_training(id)
8. Table: saved_models

Stores exported model information.

Table Name
saved_models
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Model ID
training_id	UUID	FK	—	Related training
model_name	VARCHAR(100)	NOT NULL	—	Model name
model_path	TEXT	NOT NULL	—	File location
file_type	VARCHAR(20)	NOT NULL	'pkl'	pkl/joblib
storage_type	VARCHAR(20)	NOT NULL	'local'	local/cloud
download_count	INTEGER	NOT NULL	0	Downloads
created_at	TIMESTAMP	NOT NULL	NOW()	Save time
Foreign Keys
FOREIGN KEY(training_id)
REFERENCES model_training(id)
9. Table: prediction_logs

Stores prediction history.

Table Name
prediction_logs
Column	Datatype	Constraints	Default	Description
id	UUID	PRIMARY KEY	gen_random_uuid()	Prediction ID
model_id	UUID	FK	—	Saved model
input_payload	JSONB	NOT NULL	'{}'	Input features
prediction_result	JSONB	NOT NULL	'{}'	Output
prediction_time	TIMESTAMP	NOT NULL	NOW()	Timestamp
execution_ms	INTEGER	NULL	—	Runtime
Foreign Keys
FOREIGN KEY(model_id)
REFERENCES saved_models(id)
10. ER Diagram Explanation
users
   |
   | 1:N
   ↓

projects
   |
   | 1:N
   ↓

datasets
   |
   | 1:N
   ↓

model_training
   |
   | 1:N
   ↓

leaderboard

model_training
   |
   | 1:1
   ↓

saved_models
   |
   | 1:N
   ↓

prediction_logs
11. Relationship Definitions
Source	Relation	Target
users	1:N	projects
projects	1:N	datasets
datasets	1:N	model_training
model_training	1:N	leaderboard
model_training	1:1	saved_models
saved_models	1:N	prediction_logs
12. Indexing Strategy
Users
CREATE UNIQUE INDEX idx_user_email
ON users(email);

Purpose:

Fast login lookup

Projects
CREATE INDEX idx_project_user
ON projects(user_id);

Purpose:

Retrieve user projects

Datasets
CREATE INDEX idx_dataset_project
ON datasets(project_id);
Training Sessions
CREATE INDEX idx_training_dataset
ON model_training(dataset_id);
Saved Models
CREATE INDEX idx_saved_training
ON saved_models(training_id);
Prediction Logs
CREATE INDEX idx_prediction_model
ON prediction_logs(model_id);
13. Scalability Recommendations
1. Use UUIDs

Avoid sequential IDs.

Reason:

Supports distributed systems.

2. Store ML Metadata in JSONB

Example:

{
 "selected_features":[
    "Age",
    "Salary"
 ]
}

Allows flexible schema updates.

3. Use Cloud Object Storage

Instead of storing large models in DB:

Store:

models/
best_model.pkl

Only save path in PostgreSQL.

4. Partition Prediction Logs

Prediction logs may become large.

Partition by:

month
year

Example:

prediction_logs_2026
prediction_logs_2027
5. Add Redis Cache

Cache:

leaderboard
model metadata
prediction results
6. Background Jobs

Long training tasks:

Use:

Celery
Redis Queue
Future Tables

Possible future expansion:

api_keys
notifications
training_jobs
billing
reports
audit_logs
team_members
End of Database Schema Document
