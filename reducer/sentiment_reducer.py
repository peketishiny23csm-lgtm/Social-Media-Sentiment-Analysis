#!/usr/bin/env python3
import sys

current_sentiment = None
total = 0

for line in sys.stdin:
    sentiment, count = line.strip().split("\t")

    if current_sentiment == sentiment:
        total += int(count)
    else:
        if current_sentiment is not None:
            print(f"{current_sentiment}\t{total}")

        current_sentiment = sentiment
        total = int(count)

if current_sentiment is not None:
    print(f"{current_sentiment}\t{total}")
