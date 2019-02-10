n = int(input())
while n > 0:
    points = []
    for _ in range(n):
        points.append(tuple(int(c) for c in input().split()))
    origin = points[(len(points)-1)//2]
    recentered_points = [(p[0] - origin[0], p[1] - origin[1]) for p in points]
    print(
        len([p for p in recentered_points if p[0]*p[1] > 0]),
        len([p for p in recentered_points if p[0]*p[1] < 0])
    )
    n = int(input())