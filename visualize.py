import pandas as pd
import matplotlib.pyplot as plt

# Read sentiment results
sentiment = pd.read_csv(
    "results/sentiment_counts.tsv",
    sep="\t",
    header=None,
    names=["Sentiment", "Count"]
)

# Sentiment distribution chart
plt.figure(figsize=(8, 5))
plt.bar(sentiment["Sentiment"].astype(str), sentiment["Count"])
plt.title("Social Media Sentiment Distribution")
plt.xlabel("Sentiment Label")
plt.ylabel("Number of Tweets")
plt.tight_layout()
plt.savefig("results/sentiment_distribution.png")
plt.close()

# Read word frequency results
words = pd.read_csv(
    "results/word_counts.tsv",
    sep="\t",
    header=None,
    names=["Word", "Count"]
)

# Top 20 words
top_words = words.nlargest(20, "Count").sort_values("Count")

plt.figure(figsize=(10, 7))
plt.barh(top_words["Word"], top_words["Count"])
plt.title("Top 20 Most Frequent Words in Tweets")
plt.xlabel("Frequency")
plt.tight_layout()
plt.savefig("results/top_20_words.png")
plt.close()

print("Both graphs created successfully!")
