#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split("\t", 1)

    if len(parts) == 2:
        sentiment = parts[0]
        print(f"{sentiment}\t1")
