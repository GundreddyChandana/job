#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS

# Load datasets
employment_df = pd.read_excel("employment.xlsx")
jobs_df = pd.read_csv("Jobs_Dataset.csv")
education_df = pd.read_csv("education.csv")

# Preprocess data
employment_df['skills'] = employment_df['skills'].fillna('').str.lower()
jobs_df['skills'] = jobs_df['skills'].fillna('').str.lower()
education_df['graduationPercentage'] = education_df['graduationPercentage'].fillna(0)

# Vectorize skills
tfidf = TfidfVectorizer()
skills_matrix = tfidf.fit_transform(jobs_df['skills'])

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend_jobs():
    data = request.json
    input_skills = data.get('skills', '').lower()
    experience = data.get('experience', 0)
    cgpa = data.get('cgpa', 0)
    
    input_vector = tfidf.transform([input_skills])
    similarity_scores = cosine_similarity(input_vector, skills_matrix).flatten()
    
    jobs_df['similarity'] = similarity_scores
    filtered_jobs = jobs_df[(jobs_df['minExp'] <= experience) & (jobs_df['maxExp'] >= experience)]
    recommended_jobs = filtered_jobs.sort_values(by='similarity', ascending=False).head(10)
    
    return jsonify(recommended_jobs[['jobTitle', 'skills', 'minExp', 'maxExp', 'location']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# In[ ]:






