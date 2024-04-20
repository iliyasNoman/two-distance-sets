while 1 == 1:
    line = input()
    i = 0
    j = 0
    for ch in line:
        if i == j:
            j += 1
            i = 0
        if ch == 'b':
            print(i, j)
        i += 1