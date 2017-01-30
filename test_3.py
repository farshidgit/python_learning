# Binary search on sorted list
from math import floor
from random import randint

def right_location(lst, val):  # finds the right most index where val appears in lst
    loc = 0  # location
    n = len(lst)
    while n > 1:  # length of list
        mid_point = int(floor(n/2))
        if val >= lst[mid_point]:
            lst = lst[mid_point:]
            loc += mid_point
        elif val < lst[mid_point]:
            lst = lst[:mid_point]
        n = len(lst)
    if val != lst[0]:  # at this step lst is 1 x 1
        loc = None
    return loc


def left_location(lst, val):  # finds the right most index where val appears in lst
    loc = 0  # location
    n = len(lst)
    while n > 2:  # length of list
        mid_point = int(floor(n/2))
        if val > lst[mid_point]:
            lst = lst[mid_point:]
            loc += mid_point
        elif val <= lst[mid_point]:
            lst = lst[:mid_point + 1]
        n = len(lst)
    if lst[1] == val or lst[0] == val:
        if lst[0] != val:
            loc += 1
    else:
        loc = None
    return loc


lss = [randint(1, 10) for i in range(10)]

lss.sort()
print lss
# dprint right_location(lss, 8)
print left_location(lss, 5)

