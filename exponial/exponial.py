def exponial_mod_m(n, m):
    # print('N m: ', n, m)
    if n == 1:
        return 1
    if m == 1:
        return 0
    if n < 5:
        return (n ** exponial_mod_m(n-1, 300000)) % m
    index = 0
    e = n % m
    mods = {e: 0}
    while (e * n) % m not in mods:
        index += 1
        e = (e * n) % m
        mods[e] = index
    loop_start = mods[(e*n)%m]
    loop_end = index
    # print(e, loop_start, loop_end)
    for _ in range(exponial_mod_m(n-1, loop_end-loop_start+1)):
        e = (e * n) % m
    return e

n, m = [int(x) for x in input().split()]
print(exponial_mod_m(n, m))