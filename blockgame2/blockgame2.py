def win_if_start(smaller, bigger):
    # If the number of blocks in the bigger stack
    # is a multiple of the number blocks in the smaller one,
    # you can remove them all and win
    if (bigger % smaller == 0): return True
    # else, we know what the stacks configuration will be when the smaller
    # and bigger stacks switch: (bigger % smaller, smaller)
    # we can check if that is a winning position recursively, and then
    # there are two possibilities:
    # * if bigger < smaller * 2, the only move we can do is remove <smaller>
    #   blocks from the largest stack, and then the stacks will switch.
    #   in this case, we win only if the switch is a losing position
    # * if bigger > smaller * 2, we can choose to make a move to force the
    #   switch now, or to make one that forces the other player to make
    #   the switch
    #   in this case, we always win
    win_after_switch = win_if_start(bigger % smaller, smaller)
    return True if bigger >= smaller * 2 else not win_after_switch


n, m = [int(i) for i in input().split()]
print('win' if win_if_start(min(n, m), max(n, m)) else 'lose')