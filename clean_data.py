import csv
import re

input_file = "dataset/twitter_dataset.csv"
output_file = "dataset/cleaned_tweets.tsv"

total = 0
cleaned = 0

with open(input_file, "r", encoding="utf-8") as src, \
     open(output_file, "w", encoding="utf-8") as dst:

    reader = csv.DictReader(src)
    
    for row in reader:
        total += 1

        sentiment = row["sentiment"].strip()
        tweet = row["tweet"].strip()

        if sentiment not in ("0.0", "1.0", "2.0") or not tweet:
            continue

        tweet = re.sub(r"http\S+|www\S+", "", tweet)
        tweet = re.sub(r"\s+", " ", tweet)
        tweet = tweet.replace("\t", " ")

        dst.write(sentiment + "\t" + tweet + "\n")
        cleaned += 1

print("Total records:", total)
print("Cleaned records:", cleaned)
print("Preprocessing completed successfully!")
