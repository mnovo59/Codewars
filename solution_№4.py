def move_zeros(lst):
    c = 0
    while 0 in lst:
        if 0 in lst:
            c += 1
            lst.remove(0)
    for i in range(c):
        lst.append(0)
    return lst

print(move_zeros([0, 1, 2, 0, 3]))