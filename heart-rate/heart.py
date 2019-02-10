#!/usr/bin/env python3
N = int(input())
for i in range(N):
    b, p = input().split()
    b, p = int(b), float(p)
    print((b-1)*60/p, b*60/p, (b+1)*60/p)
