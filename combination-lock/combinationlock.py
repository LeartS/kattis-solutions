import sys

def degrees(start_position, end_position, clockwise=True):
    if clockwise:
        return (start_position - end_position) % 40 * 9
    return (end_position - start_position) % 40 * 9

for start, f, s, t in (map(int, l.split()) for l in sys.stdin.readlines()[:-1]):
    print(1080 + degrees(start, f) + degrees(f, s, False) + degrees(s, t))