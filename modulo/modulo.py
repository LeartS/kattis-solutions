#!/usr/bin/env python3
import sys
print(len(set(int(i) % 42 for i in sys.stdin.readlines())))
