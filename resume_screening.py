import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
df = pd.read_csv("Resume.csv")

# Keep required columns
df = df[["Resume_str", "Category"]]

# Remove missing values
df = df.dropna()

# Example Job Description
job_description = """
Looking for a Machine Learning Engineer with skills in
Python, Machine Learning, Data Analysis, SQL,
Deep Learning and Artificial Intelligence.
"""

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")

resume_vectors = vectorizer.fit_transform(df["Resume_str"])

job_vector = vectorizer.transform([job_description])

# Similarity Scores
scores = cosine_similarity(job_vector, resume_vectors)

df["Match Score"] = scores[0] * 100

# Rank Candidates
ranked_df = df.sort_values(
    by="Match Score",
    ascending=False
)

print("\nTop 10 Candidates:\n")

for i, row in ranked_df.head(10).iterrows():
    print("-" * 50)
    print("Category:", row["Category"])
    print("Match Score:", round(row["Match Score"], 2), "%")
skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "power bi",
    "excel",
    "java",
    "c++"
]

top_resume = ranked_df.iloc[0]["Resume_str"].lower()

found_skills = []
missing_skills = []

for skill in skills:
    if skill in top_resume:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

print("\nFound Skills:")
print(found_skills)

print("\nMissing Skills:")
print(missing_skills)