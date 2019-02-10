def find_next(p, q):
    """
    1. Go up until we are at a left child or at the root
    2. Go to right sibling (or do nothing if at root)
    3. Go down by always taking the left child until we are back at the
       starting depth, or starting depth + 1 if we reached the root.
    """
    initial_p = p
    # ascent
    # shorcut: the parent node of a right child is p-q, p,
    # which means we can go up all right nodes by
    # seeing how many times we can subtract q
    depth = (p // q)
    p, q = max(p % q, 1), q
    # if root, shortcut to final result
    if p == q == 1:
        return 1, initial_p+1
    # move right
    p, q = q, q-p
    # descent (only q changes as we go down by going left)
    return p, q + p * depth


p = int(input())
for _ in range(p):
    i, pq = input().split(' ')
    p, q = [int(x) for x in pq.split('/')]
    print('{} {}/{}'.format(i, *find_next(p, q)))