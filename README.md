# Resume Screening and Candidate Ranking System

## Objective
This project builds a Machine Learning-based resume screening system that automatically evaluates resumes against a job description, ranks candidates based on relevance, and identifies missing skills.

## Dataset
Resume Dataset (Kaggle)

Dataset Link:
https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- VS Code

## Features
- Resume text preprocessing
- Job description matching
- Similarity score calculation
- Candidate ranking
- Skill extraction
- Missing skill identification

## Workflow
1. Load resume dataset
2. Clean and preprocess resume text
3. Convert text into TF-IDF vectors
4. Parse job description
5. Calculate cosine similarity scores
6. Rank candidates based on job relevance
7. Extract available skills
8. Identify missing skills

## Example Output

Top 10 Candidates:
- Category: Data Science
- Match Score: 20.31%

Found Skills:
- Python
- SQL

Missing Skills:
- Deep Learning
- Power BI

## Business Benefits
- Reduces recruiter workload
- Speeds up resume screening
- Improves candidate shortlisting
- Highlights skill gaps
- Supports data-driven hiring decisions

## Project Structure

FUTURE_ML_03
│
├── resume_screening.py
├── README.md
├── output.png
└── skills.png

## Conclusion
This system automatically screens resumes, compares them with job requirements, ranks candidates by relevance, and identifies missing skills. It can help recruiters make faster and more informed hiring decisions.