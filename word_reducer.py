#!/usr/bin/env python3
import sys

current_word = None
total = 0

for line in sys.stdin:
    word, count = line.strip().split("\t")

    if current_word == word:
        total += int(count)
    else:
        if current_word is not None:
            print(f"{current_word}\t{total}")

        current_word = word
        total = int(count)

if current_word is not None:
    print(f"{current_word}\t{total}")
