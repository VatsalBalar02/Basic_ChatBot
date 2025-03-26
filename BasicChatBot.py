# -*- coding: utf-8 -*-
"""chatbotAssingment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R_vj-84LHYDF6av1RnbmcNLMChEwJDNW

# Install Required Libraries
"""

# pip install pandas numpy nltk scikit-learn joblib

"""#Import Necessary Library"""

import pandas as pd
import numpy as np
import nltk
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""#Load and Preprocess User *Queries*"""

data = {
    "query": [
        "How can I register my startup?",
        "Best funding options for new startups?",
        "What government schemes support startups?",
        "Help me create a marketing plan.",
        "Startup-friendly banks in India.",
        "Steps to get GST registration.",
        "Find co-working spaces in Delhi.",
        "Legal requirements for tech startups.",
        "I need a pitch deck template.",
        "Tips for startup valuation."
    ],
    "category": [
        "Registration & Legal",
        "Funding",
        "Funding",
        "Business Strategy",
        "Funding",
        "Registration & Legal",
        "Resources & Networking",
        "Registration & Legal",
        "Resources & Networking",
        "Business Strategy"
    ]
}

df = pd.DataFrame(data)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

df['proccessed_query'] = df['query'].apply(preprocess_text)

"""#Convert Text to Features"""

vectorize = TfidfVectorizer()
x = vectorize.fit_transform(df['proccessed_query'])
y = df['category']

joblib.dump(vectorize, 'vectorizer.pkl')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

"""#Train a Chatbot Model"""

model = MultinomialNB()
model.fit(x_train, y_train)

joblib.dump(model, 'chatbot_model.pkl')

# y_pred = model.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy}")
# print('classification replort:\n', classification_report(y_test, y_pred))

"""#User Interaction Analysis"""

category_counts = df['category'].value_counts()
print("\nQuery Frequency per Category:\n", category_counts)

user_feedback = {"Registration & Legal": 80, "Funding": 60, "Business Strategy": 50, "Resources & Networking": 40}
total_queries = sum(user_feedback.values())

satisfaction_score = {category: (count / total_queries) * 100 for category, count in user_feedback.items()}
print("\nUser Satisfaction Score:\n", satisfaction_score)

resolved_queries = {"Registration & Legal": 70, "Funding": 50, "Business Strategy": 45, "Resources & Networking": 35}
resolution_rate = {category: (resolved_queries[category] / user_feedback[category]) * 100 for category in user_feedback}
print("\nResolution Rate:\n", resolution_rate)

"""# Improve Chatbot Responses Using Reinforcement Learning"""

feedback_data = pd.DataFrame({
    "query": df["query"],
    "category": df["category"],
    "feedback": [1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
})

filtered_df = feedback_data[feedback_data["feedback"] == 1]
X_filtered = vectorize.transform(filtered_df['query'])
y_filtered = filtered_df['category']

model.fit(X_filtered, y_filtered)
joblib.dump(model, 'improved_chatbot_model.pkl')

"""#Deploy and Use the Model"""

vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('improved_chatbot_model.pkl')

def predict_category(user_query):
    processed_query = preprocess_text(user_query)
    query_vector = vectorizer.transform([processed_query])
    category = model.predict(query_vector)[0]
    return category

user_query = "I need a pitch deck template."
print("\nPredicted Category:", predict_category(user_query))

