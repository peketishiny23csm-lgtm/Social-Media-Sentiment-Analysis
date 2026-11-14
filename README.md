# Social Media Sentiment Analysis

## Project Overview
This project analyzes large-scale social media data using Hadoop MapReduce and Machine Learning techniques. It processes tweets, analyzes sentiment labels, identifies frequently used words, and visualizes the results.

## Objectives
- Analyze millions of social media tweets.
- Perform distributed data processing using Hadoop.
- Calculate sentiment distribution.
- Identify the most frequently used words.
- Classify tweets using Naive Bayes.

## Technologies Used
- Python
- Hadoop 3.3.6
- HDFS
- MapReduce
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Matplotlib

## Dataset
Twitter Sentiment Dataset containing approximately 3.14 million records.

## Implementation
1. Dataset collection and preprocessing.
2. Uploading cleaned data to HDFS.
3. Sentiment analysis using Hadoop MapReduce.
4. Word frequency analysis using MapReduce.
5. Data visualization.
6. Naive Bayes model training and evaluation.
7. Sentiment prediction for new tweets.

## Results
- Total tweets processed: 3,142,209
- Naive Bayes accuracy: 76.94%
- Sentiment distribution graph generated.
- Top 20 frequent words graph generated.
- New tweet prediction successfully tested.

## Project Structure
- `mapper/` – MapReduce mapper scripts.
- `reducer/` – MapReduce reducer scripts.
- `results/` – Analysis outputs and graphs.
- `clean_data.py` – Data preprocessing.
- `train_model.py` – Model training.
- `predict.py` – Sentiment prediction.
- `visualize.py` – Graph generation.

## Note
The dataset and trained model files are excluded from this repository because of their large size.

## Author
Peketi Shiny
