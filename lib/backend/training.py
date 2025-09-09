import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load your dataset
data = pd.read_csv('lib/backend/twitter-hate-speech2.csv')  # Replace with the path to your CSV file

# Split the data into features (X) and target labels (y)
X = data['tweet']
y = data['class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer and fit it on the training data
tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

# Train a classification model (Logistic Regression in this example)
model = LogisticRegression(class_weight='balanced', penalty='l2', C=0.01)
model.fit(X_train_tfidf, y_train)

# Save the trained model and vectorizer for later use
joblib.dump(model, 'hate_speech_classifier.pkl')
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')

# Evaluate the model on the test set (you can use metrics like accuracy, precision, recall, F1-score, etc.)
X_test_tfidf = tfidf_vectorizer.transform(X_test)
accuracy = model.score(X_test_tfidf, y_test)
print(f"Test Accuracy: {accuracy}")
