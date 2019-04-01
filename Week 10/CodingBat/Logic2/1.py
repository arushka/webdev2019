def make_bricks(small, big, goal):
    if (big != 0 and goal / 5 == big and goal % (big * 5) == 0) or (small != 0 and small > goal):
        return True
    if goal == 0:
        return True
    if (goal / 5 <= big and (goal - big * 5) % 5 <= small):
        return True
    if 0 <= (goal - big * 5) <= small and big != 0:
        return True
    return False