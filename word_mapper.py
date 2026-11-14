#!/usr/bin/env python3
import sys
import re

stop_words = {
    "the", "is", "a", "an", "and", "to", "of", "in", "for",
    "on", "it", "this", "that", "my", "i", "you", "are",
    "was", "with", "at", "be", "have", "has", "not"
}

for line in sys.stdin:
    parts = line.strip().split("\t", 1)

    if len(parts) == 2:
        tweet = parts[1].lower()
        words = re.findall(r"[a-z]+", tweet)

        for word in words:
            if word not in stop_words and len(word) > 2:
                print(f"{word}\t1")
