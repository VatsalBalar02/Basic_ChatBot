# Startup Chatbot: AI-Powered Query Categorization

## Project Overview
This Python-based chatbot is designed to help startups by automatically categorizing user queries related to various startup needs, such as registration, funding, business strategy, and networking resources.

## Features
- Intelligent query categorization using machine learning
- Text preprocessing with stopword removal
- TF-IDF vectorization
- Naive Bayes classification
- Model improvement through reinforcement learning
- User feedback analysis

## Requirements
- Python 3.x
- Libraries:
  - pandas
  - numpy
  - nltk
  - scikit-learn
  - joblib

## Installation
1. Clone the repository
2. Install required libraries:
   ```
   pip install pandas numpy nltk scikit-learn joblib
   ```
3. Download NLTK stopwords:
   ```python
   import nltk
   nltk.download('stopwords')
   ```

## How It Works
1. **Data Preprocessing**: Converts user queries to lowercase, removes punctuation, and filters stopwords
2. **Feature Extraction**: Uses TF-IDF vectorization to convert text to numerical features
3. **Model Training**: Trains a Multinomial Naive Bayes classifier
4. **Category Prediction**: Predicts query categories based on input text

## Categories
- Registration & Legal
- Funding
- Business Strategy
- Resources & Networking

## Usage
```python
from BasicChatBot import predict_category

user_query = "I need a pitch deck template."
category = predict_category(user_query)
print(category)  # Outputs: Resources & Networking
```

## Performance Metrics
- Tracks query frequency
- Measures user satisfaction scores
- Calculates query resolution rates

## Model Improvement
- Incorporates user feedback
- Uses reinforcement learning techniques to refine categorization

## Future Enhancements
- Expand query dataset
- Implement more advanced NLP techniques
- Add more detailed category handling
- Improve model accuracy


## Acknowledgments
- Built using scikit-learn machine learning library
- Inspired by startup ecosystem support
