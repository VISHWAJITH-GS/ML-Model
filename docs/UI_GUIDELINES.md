UI/UX Design Guidelines
AutoML Web Platform using Ensemble Learning

Document Version: 1.0
Product Type: AI-Based AutoML Platform
Design Inspiration: Google AutoML, Kaggle, H2O AI
Design Style: Modern AI Dashboard
Status: Design System Draft

1. Design Philosophy

The AutoML platform should feel:

Intelligent
Minimal
Fast
Data-focused
Professional
Beginner-friendly
Enterprise-ready

The experience should reduce complexity while giving users confidence in machine learning decisions.

Design principles:

Simplicity First

Avoid unnecessary complexity.

Progressive Disclosure

Show advanced features only when needed.

Data-Centric Interfaces

Data and results should be visually prioritized.

Explainability

Always explain automated decisions.

Example:

Best model selected:
XGBoost (97% accuracy)
Reason:
Highest performance score
Reduce User Decisions

Avoid:

Choose 15 ML algorithms manually

Prefer:

System automatically selected best model
2. Color Palette

Theme:

Modern AI Dashboard

Primary Colors
Purpose	Color
Primary Blue	#2563EB
AI Accent	#7C3AED
Success	#10B981
Warning	#F59E0B
Error	#EF4444
Neutral Colors
Purpose	Color
Background	#F8FAFC
Card	#FFFFFF
Border	#E2E8F0
Text Primary	#0F172A
Text Secondary	#64748B
Usage Rules

Primary blue:

buttons
links
active elements

Purple accent:

AI-generated results
highlighted intelligence sections

Green:

success
completed training
3. Typography

Font style:

Inter

Fallback:

system-ui
Typography Scale
Element	Size	Weight
Hero title	36px	Bold
Page title	30px	Semi-bold
Section title	24px	Medium
Card title	18px	Medium
Body	16px	Regular
Caption	14px	Regular

Rules:

Maximum 3 font weights
Avoid excessive capitalization
Maintain spacing consistency
4. Layout Structure

Use:

Sidebar + Main Content Layout

Structure:

+----------------------------------+

Sidebar | Main Dashboard Area

+----------------------------------+
Layout Grid

Desktop:

12-column grid

Tablet:

8-column grid

Mobile:

4-column grid
5. Navigation Design

Sidebar navigation:

Dashboard
Upload Dataset
Projects
Leaderboard
Predictions
Settings

Rules:

Fixed sidebar
Active state highlighted
Icons required
Breadcrumb support

Sidebar Width:

260px

Collapsed:

80px
6. Dashboard Design

Dashboard should immediately answer:

What dataset is loaded?
Training status?
Best model?
Performance?
Available actions?

Dashboard Layout

------------------------------------------------

Dataset Summary Card

------------------------------------------------

Leaderboard Card

------------------------------------------------

Charts

------------------------------------------------

Best Model Card

------------------------------------------------
Dashboard Widgets

Include:

Dataset summary

Display:

rows
columns
missing values
Best model widget

Display:

🏆 XGBoost

Accuracy:97%
Model performance widget

Show:

ranking
score
metrics
7. Dataset Upload Page

Upload area:

Large drag-and-drop component

Supported:

CSV
XLSX

Upload card:

+-------------------------+

Drag Dataset Here

or

Browse Files

CSV | XLSX

+-------------------------+

After upload:

Show:

file name
size
preview
8. Charts and Visualization Guidelines

Supported charts:

Histogram

Purpose:

Feature distribution

Correlation Heatmap

Purpose:

Relationship analysis

Bar Charts

Purpose:

Model comparison

Pie Charts

Purpose:

Data categories

Training Progress

Use:

Progress bars

Rules:

Avoid:

3D charts
excessive colors
9. Model Leaderboard Page

Purpose:

Rank trained models.

Layout:

Rank

Model Name

Metric

Score

Action

Example:

Rank	Model	Accuracy
🥇	XGBoost	97%
🥈	RandomForest	95%
🥉	SVM	91%

Highlight:

Best model:

Background:
light green
10. Responsive Design

Desktop:

≥1200px

Tablet:

768–1199px

Mobile:

<768px

Rules:

Desktop:

Sidebar visible

Mobile:

Sidebar becomes drawer menu

Cards:

Stack vertically

Tables:

Horizontal scroll

11. Accessibility Standards

Must comply with:

WCAG 2.1

Requirements:

Color contrast:

Minimum:

4.5:1

Support:

keyboard navigation
screen readers
aria labels
focus indicators

Buttons:

Minimum size:

44x44px
12. Error States

Errors must:

explain problem
suggest action

Example:

Dataset upload failed

Please upload CSV or XLSX

Avoid:

Error 403

Use:

Icons + message

13. Loading States

Use:

Skeleton loaders

Example:

████████████

██████

██████████

Training:

Display:

Training models...

Random Forest ✔

XGBoost running...

Progress:

65%
14. Empty States

Avoid blank pages.

Example:

Leaderboard:

No models available

Upload dataset to begin

Dashboard:

No dataset loaded

Include:

illustration
CTA button
15. UI Component Guidelines
Input Fields

Rules:

rounded corners
labels required
validation below field
Dropdowns

Searchable if:

10 options

Modals

Maximum:

500px width
16. Button Styles

Primary Button:

Blue background

White text

Use:

upload
submit
train

Secondary:

White background

border

Danger:

Red background

Sizes:

Small:

32px

Medium:

40px

Large:

48px
17. Card Layout Rules

Cards:

padding:24px

border-radius:16px

shadow:small

Structure:

Title

Description

Content

Actions
18. Table Design

Use:

Sticky headers

Columns:

sortable
searchable

Rows:

Hover effect

Pagination:

Required

19. Sidebar Behavior

Desktop:

Persistent

Tablet:

Collapsible

Mobile:

Drawer navigation

Active page:

Blue indicator

Icons:

Required

20. Wireframe Descriptions
Dashboard Wireframe
+------------------------------------------------+

Sidebar

+------------------------------------------------+

Dataset Summary

+------------------------------------------------+

Leaderboard

+------------------------------------------------+

Charts

+------------------------------------------------+

Best Model

+------------------------------------------------+
Upload Page Wireframe
+--------------------------------+

Drag & Drop Upload Area

+--------------------------------+

Dataset Preview

+--------------------------------+

Column Selection

+--------------------------------+

Train Button

+--------------------------------+
Leaderboard Wireframe
+--------------------------------+

Rank | Model | Score

+--------------------------------+

Model Cards

+--------------------------------+

Download Best Model

+--------------------------------+
Final UI Principles

✅ Simple UI
✅ Data-first design
✅ Responsive layouts
✅ AI-focused interactions
✅ Accessibility support
✅ Progressive disclosure
✅ Visual consistency
✅ Explainable automation

End of UI/UX Guidelines DocumentUI/UX Design Guidelines
AutoML Web Platform using Ensemble Learning

Document Version: 1.0
Document Type: UI/UX Design System & Guidelines
Project: AutoML Web Platform using Ensemble Learning
Design Style: Modern AI Dashboard
Inspired By: Google AutoML, Kaggle, H2O AI
Status: Draft

1. Introduction
Purpose

This document defines the UI/UX standards and design system for the AutoML platform. The objective is to create a modern AI-first experience that simplifies machine learning workflows for both technical and non-technical users.

The platform should feel:

Intelligent
Minimal
Fast
Professional
Data-driven
Beginner-friendly
Enterprise-grade
2. Design Philosophy

The product design should follow these principles:

2.1 Simplicity First

Hide complexity behind intelligent automation.

Avoid:

Technical overload
Excessive options
Dense interfaces

Prefer:

Clear actions
Guided workflows
Minimal decision making
2.2 Progressive Disclosure

Show basic actions first.

Advanced options should appear only when needed.

Example:

Basic View:

Upload Dataset
Select Target
Train Models

Advanced View:

Feature Selection
Encoding Options
Hyperparameter Settings
2.3 Explainable Intelligence

The platform must explain AI decisions.

Example:

Best Model: XGBoost
Accuracy: 97%

Reason:
Highest prediction performance
2.4 Data-First Interfaces

The interface should prioritize:

datasets
metrics
charts
model insights
3. Color Palette

Theme:

Modern AI Dashboard

Primary Colors
Role	Color	Usage
Primary Blue	#2563EB	Main actions
AI Purple	#7C3AED	AI highlights
Success Green	#10B981	Completed actions
Warning Amber	#F59E0B	Warnings
Error Red	#EF4444	Failures
Neutral Colors
Role	Color
Background	#F8FAFC
Card Background	#FFFFFF
Border	#E2E8F0
Primary Text	#0F172A
Secondary Text	#64748B
Color Usage Rules

Blue:

buttons
links
active elements

Purple:

AI recommendations
intelligent selections

Green:

success indicators
completed training

Red:

validation errors
4. Typography

Primary Font:

Inter

Fallback:

system-ui
Typography Scale
Element	Size	Weight
Hero Heading	36px	Bold
Page Heading	30px	SemiBold
Section Heading	24px	Medium
Card Title	18px	Medium
Body Text	16px	Regular
Caption	14px	Regular

Rules:

Maximum 3 font weights
Maintain spacing consistency
Avoid full uppercase paragraphs
5. Layout Structure

The application uses:

Sidebar + Main Content Layout

Desktop Layout:

+--------------------------------------------------+

Sidebar | Main Content Area

+--------------------------------------------------+

Grid System:

Desktop:

12 columns

Tablet:

8 columns

Mobile:

4 columns

Spacing Scale

Value	Usage
8px	Small spacing
16px	Component spacing
24px	Card spacing
32px	Section spacing
6. Navigation Design

Navigation should remain consistent across all pages.

Sidebar Navigation
Dashboard

Upload Dataset

Projects

Leaderboard

Predictions

Settings

Sidebar Rules:

Fixed position on desktop
Collapsible on tablet
Drawer menu on mobile
Active route highlighted
Icons mandatory

Sidebar Width:

Expanded:

260px

Collapsed:

80px
7. Dashboard Design

Dashboard answers:

What dataset is loaded?
What model performed best?
Training status?
Metrics?
Available actions?
Dashboard Layout
+---------------------------------------+

Dataset Summary

+---------------------------------------+

Leaderboard

+---------------------------------------+

Performance Charts

+---------------------------------------+

Best Model Widget

+---------------------------------------+
Dashboard Components
Dataset Summary Card

Display:

Rows
Columns
Missing values
Best Model Widget

Display:

🏆 XGBoost

Accuracy:97%
Training Status Widget

Display:

completed
running
failed
8. Dataset Upload Page

Primary entry point of application.

Upload Area:

Large drag-and-drop component.

Supported:

CSV
XLSX

Upload Wireframe

+--------------------------------+

Drag Dataset Here

or

Browse Files

CSV | XLSX

+--------------------------------+

After upload:

Display:

file name
size
preview rows
upload status
9. Charts and Visualization Guidelines

Purpose:

Convert model output into understandable visuals.

Supported Visualizations:

Histogram

Use:

Feature distribution

Correlation Heatmap

Use:

Feature relationship analysis

Bar Charts

Use:

Model performance comparison

Pie Charts

Use:

Class distribution

Progress Indicators

Use:

Training progress

Rules:

Avoid:

3D charts
excessive colors
chart clutter
10. Model Leaderboard Page

Purpose:

Display ranking of trained models.

Layout:

Rank	Model	Metric	Score	Action
🥇	XGBoost	Accuracy	97%	Download
🥈	Random Forest	Accuracy	95%	Download
🥉	SVM	Accuracy	91%	Download

Best Model Highlight:

Background:

Light Green
11. Responsive Design

Desktop:

≥1200px

Tablet:

768–1199px

Mobile:

<768px

Rules:

Desktop:

Sidebar visible

Tablet:

Sidebar collapses

Mobile:

Drawer navigation

Cards:

Stack vertically

Tables:

Enable horizontal scrolling

12. Accessibility Standards

Comply with:

WCAG 2.1

Requirements:

Color Contrast

Minimum:

4.5:1

Support:

keyboard navigation
focus states
aria labels
screen readers

Buttons minimum size:

44x44px
13. Error States

Errors should:

explain problem
provide action
avoid technical jargon

Good Example:

Upload failed

Please upload CSV or XLSX files only

Bad Example:

Error 403

Use:

icons
illustrations
CTA buttons
14. Loading States

Use:

Skeleton loaders

Example:

████████████

████████

███████

Training Loader:

Training Models...

Random Forest ✔

XGBoost Running...

Progress Example:

65%
15. Empty States

Avoid empty screens.

Leaderboard Empty State

No trained models available

Upload a dataset to begin

Dashboard Empty State

No dataset selected

Include:

illustration
explanation
CTA
16. UI Component Guidelines
Input Fields

Rules:

labels mandatory
placeholder optional
validation below field
Dropdowns

Use search when:

More than:

10 options
Modals

Maximum width:

500px
17. Button Styles

Primary Button

Style:

Blue background

White text

Use:

upload
train
submit

Secondary Button

Style:

White background

Gray border

Danger Button

Style:

Red background

Sizes:

Small:

32px

Medium:

40px

Large:

48px
18. Card Layout Guidelines

Card Style:

padding:24px;

border-radius:16px;

box-shadow:small;

Card Structure:

Title

Description

Content

Actions
19. Table Design Guidelines

Rules:

sticky headers
sortable columns
searchable tables
pagination enabled
row hover effect

Table Example:

Rank | Model | Accuracy | Action
20. Sidebar Behavior

Desktop:

Persistent

Tablet:

Collapsible

Mobile:

Drawer navigation

Sidebar Features:

icons
active indicator
route highlighting
21. Wireframe Descriptions
Dashboard
+------------------------------------------------+

Sidebar

+------------------------------------------------+

Dataset Summary

+------------------------------------------------+

Leaderboard

+------------------------------------------------+

Charts

+------------------------------------------------+

Best Model Widget

+------------------------------------------------+
Upload Page
+--------------------------------+

Dataset Upload Area

+--------------------------------+

Preview Table

+--------------------------------+

Feature Selection

+--------------------------------+

Train Button

+--------------------------------+
Leaderboard Page
+--------------------------------+

Rank | Model | Accuracy

+--------------------------------+

Charts

+--------------------------------+

Download Model

+--------------------------------+
Final UI Principles

✅ Clean interfaces
✅ AI-focused design
✅ Responsive layout
✅ Minimal user effort
✅ Explainable automation
✅ Data-first workflow
✅ Accessibility support
✅ Enterprise-grade consistency

End of UI/UX Design Guidelines Document