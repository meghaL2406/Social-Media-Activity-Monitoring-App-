import joblib

# Load the trained model and TF-IDF vectorizer
model = joblib.load('hate_speech_classifier.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to classify user input
def classify_text(user_input):
    # Transform the user input using the loaded vectorizer
    user_input_tfidf = tfidf_vectorizer.transform([user_input])

    # Predict the class label using the loaded model
    predicted_label = model.predict(user_input_tfidf)

    # Return the predicted class label
    return  predicted_label[0]
    



