#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

jobs_df = pd.read_csv("Jobs_Dataset.csv")
employment_df = pd.read_excel("employment.xlsx")
education_df = pd.read_csv("education.csv")


# In[3]:


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_skills = data.get("skills", [])
    # Implement job filtering logic here
    recommended_jobs = jobs_df[jobs_df['skills'].str.contains('|'.join(user_skills), na=False)]
    return jsonify(recommended_jobs.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)


# In[5]:


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # ✅ Keep only one definition
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




