import csv
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

tweets = []
labels = []

# Load dataset
with open("dataset/twitter_dataset.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        text = row["tweet"].strip()
        label = row["sentiment"].strip()

        if text and label in ("0.0", "1.0", "2.0"):
            tweets.append(text)
            labels.append(label)

print("Total tweets:", len(tweets))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    tweets, labels, test_size=0.2, random_state=42, stratify=labels
)

# Convert text into numerical features
vectorizer = TfidfVectorizer(max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate model
predictions = model.predict(X_test_vec)

print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Save model
joblib.dump(model, "results/naive_bayes_model.pkl")
joblib.dump(vectorizer, "results/tfidf_vectorizer.pkl")

print("\nModel training completed successfully!")
