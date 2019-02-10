#!/usr/bin/env python3
import sys

[print('skipped' if x.strip() == 'P=NP' else sum(int(n) for n in x.split('+'))) for x in sys.stdin.readlines()[1:]]
