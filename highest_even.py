def highest_even(li):
    cur_highest = 0
    for i in li:
        if i%2 == 0 and i > cur_highest:
            cur_highest = i
    return(cur_highest)


some_list = [10, 21, 3, 4, 9, 2, 22, 7, 12, 11]
print(highest_even(some_list))
