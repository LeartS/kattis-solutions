#!/usr/bin/env python3

def game (first_guess):
    min_ = 1
    max_ = 10
    guess = first_guess
    dishonest = False
    while True:
        response = input().strip()
        if response == 'too high':
            max_ = min(max_, guess - 1)
        elif response == 'too low':
            min_ = max(min_, guess + 1)
        else:  # right on
            if min_ <= guess <= max_:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')
            return
        guess = int(input())

first_guess = int(input())
while first_guess != 0:
    game(first_guess)
    first_guess = int(input())



