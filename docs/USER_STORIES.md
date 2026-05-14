User Stories Document
AutoML Web Platform using Ensemble Learning

Methodology: Agile Scrum
Project: AutoML Web Platform using Ensemble Learning
Version: 1.0
Status: Draft

Epic 1: Dataset Management
Story ID: US-001
User Story

As a user,
I want to upload CSV datasets,
So that I can train machine learning models using my own data.

Acceptance Criteria
User can upload .csv files
File validation occurs before processing
Upload success message is displayed
Invalid formats are rejected
Priority

High

Dependencies

None

Story ID: US-002
User Story

As a user,
I want to upload Excel files,
So that I can use spreadsheet datasets directly.

Acceptance Criteria
Support .xlsx
Reject unsupported files
Show upload status
Priority

High

Dependencies

US-001

Story ID: US-003
User Story

As a user,
I want to preview uploaded datasets,
So that I can verify uploaded data before training.

Acceptance Criteria
Display first rows of dataset
Show row count
Show column names
Priority

High

Dependencies

US-001

Epic 2: Dataset Analysis
Story ID: US-004
User Story

As a user,
I want the system to detect numerical and categorical columns,
So that I understand dataset structure automatically.

Acceptance Criteria
Identify data types
Show column classifications
Priority

High

Dependencies

US-003

Story ID: US-005
User Story

As a user,
I want the system to detect missing values,
So that I understand data quality issues.

Acceptance Criteria
Display null count
Highlight affected columns
Priority

High

Dependencies

US-003

Epic 3: Feature Selection
Story ID: US-006
User Story

As a user,
I want to select input features,
So that I can control model training variables.

Acceptance Criteria
Multi-select supported
Prevent empty selection
Priority

High

Dependencies

US-003

Story ID: US-007
User Story

As a user,
I want to select a target column,
So that the platform knows prediction output.

Acceptance Criteria
Single target selection
Validation required
Priority

High

Dependencies

US-006

Epic 4: Automated Preprocessing
Story ID: US-008
User Story

As a user,
I want automatic preprocessing,
So that I do not manually clean datasets.

Acceptance Criteria
Handle missing values
Encode categories
Scale numerical values
Priority

High

Dependencies

US-007

Story ID: US-009
User Story

As a user,
I want duplicate rows removed automatically,
So that dataset quality improves.

Acceptance Criteria
Detect duplicates
Remove duplicate records
Priority

Medium

Dependencies

US-008

Epic 5: Automated Training
Story ID: US-010
User Story

As a user,
I want the platform to automatically train multiple models,
So that I don't manually test algorithms.

Acceptance Criteria
Train multiple ML models
Display training status
Priority

High

Dependencies

US-008

Story ID: US-011
User Story

As a user,
I want automatic problem type detection,
So that I don't manually select classification or regression.

Acceptance Criteria
Detect categorical output
Detect numerical output
Priority

High

Dependencies

US-010

Story ID: US-012
User Story

As a user,
I want ensemble models included,
So that prediction performance improves.

Acceptance Criteria

Include:

Random Forest
XGBoost
Boosting models
Priority

Medium

Dependencies

US-010

Epic 6: Evaluation and Comparison
Story ID: US-013
User Story

As a user,
I want all model performances compared,
So that I understand which model performs best.

Acceptance Criteria

Display:

Accuracy
Precision
Recall
F1 score
Priority

High

Dependencies

US-010

Story ID: US-014
User Story

As a user,
I want a leaderboard view,
So that I can rank trained models.

Acceptance Criteria
Sort models
Show scores
Highlight best model
Priority

Medium

Dependencies

US-013

Story ID: US-015
User Story

As a user,
I want automatic best model selection,
So that I don't analyze metrics manually.

Acceptance Criteria
Highest metric selected
Winner highlighted
Priority

High

Dependencies

US-014

Epic 7: Export and Prediction
Story ID: US-016
User Story

As a user,
I want to download trained models,
So that I can reuse them later.

Acceptance Criteria
Download .pkl
Validate file generation
Priority

High

Dependencies

US-015

Story ID: US-017
User Story

As a user,
I want metadata with downloaded models,
So that I know required feature order.

Acceptance Criteria

Generate:

feature names
model type
metrics
Priority

Medium

Dependencies

US-016

Story ID: US-018
User Story

As a developer,
I want a prediction API,
So that saved models can predict future values.

Acceptance Criteria

API accepts JSON input

Returns:

{
"prediction":"value"
}
Priority

High

Dependencies

US-016

Epic 8: Visualization Dashboard
Story ID: US-019
User Story

As a user,
I want visual charts and graphs,
So that I understand dataset patterns.

Acceptance Criteria

Include:

histograms
correlation heatmaps
model charts
Priority

Medium

Dependencies

US-003

Story ID: US-020
User Story

As a user,
I want performance charts,
So that I can compare model quality visually.

Acceptance Criteria

Display:

bar charts
score trends
Priority

Medium

Dependencies

US-013

Epic 9: Authentication
Story ID: US-021
User Story

As a user,
I want account registration,
So that my projects can be saved.

Acceptance Criteria
Register account
Email validation
Priority

Low

Dependencies

None

Story ID: US-022
User Story

As a user,
I want secure login,
So that my project data stays private.

Acceptance Criteria
Password authentication
JWT token support
Priority

Low

Dependencies

US-021

Epic 10: Error Handling
Story ID: US-023
User Story

As a user,
I want clear upload error messages,
So that I understand issues immediately.

Acceptance Criteria

Examples:

invalid format
upload failure
file corruption
Priority

High

Dependencies

US-001

Story ID: US-024
User Story

As a user,
I want training failure messages,
So that I know when model generation fails.

Acceptance Criteria

Display:

Training failed. Please verify your dataset.
Priority

High

Dependencies

US-010

Story Dependency Flow
US-001
   ↓
US-003
   ↓
US-006
   ↓
US-007
   ↓
US-008
   ↓
US-010
   ↓
US-013
   ↓
US-014
   ↓
US-015
   ↓
US-016
Priority Summary
Priority	Count
High	16
Medium	6
Low	2
End of User Stories Document