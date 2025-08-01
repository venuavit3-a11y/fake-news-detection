# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset: text + label (0 = Real news, 1 = Fake news)
data = {
    'text': [
        "The economy is growing steadily with new job opportunities.",
        "Aliens have landed in New York City, government confirms!",
        "New health policies to improve hospital care announced today.",
        "Congratulations! You won $1,000,000. Click here to claim now!",
        "Climate change effects worsen every year, scientists warn.",
        "Miracle cure for diabetes discovered, doctors shocked!"
    ],
    'label': [0, 1, 0, 1, 0, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split dataset into training and testing sets (70/30)
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.3, random_state=42
)

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))