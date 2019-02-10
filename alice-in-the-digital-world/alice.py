#!/usr/bin/env python3

def test_case():
    n, m = (int(x) for x in input().split())
    numbers = list(int(x) for x in input().split())
    best = 0
    current = 0
    valid = False
    since_last_m = 0
    for e in numbers:
        if e < m:
            best = current if valid and current > best else best
            valid = False
            current = 0
            since_last_m = 0
        elif e == m and not valid:
            valid = True
            current += e
        elif e == m and valid:
            best = current if current > best else best
            current = since_last_m + e
            since_last_m = 0
        else:
            current += e
            if valid:
                since_last_m += e
    best = current if valid and current > best else best
    print(best)

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        test_case()