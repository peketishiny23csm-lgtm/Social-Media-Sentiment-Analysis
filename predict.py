import joblib

model = joblib.load("results/naive_bayes_model.pkl")
vectorizer = joblib.load("results/tfidf_vectorizer.pkl")

print("Social Media Sentiment Prediction")

tweet = input("Enter a tweet: ")

tweet_vector = vectorizer.transform([tweet])
prediction = model.predict(tweet_vector)

print("Predicted sentiment label:", prediction[0])
