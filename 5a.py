ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
rj = dict()
for red in sve:
    red = red.split()
    y1, x1 = list(map(int, red[0].split(',')))
    y2, x2 = list(map(int, red[2].split(',')))
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, y) in rj:
                rj[(x1, y)] += 1
            else:
                rj[(x1, y)] = 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if (x, y1) in rj:
                rj[(x, y1)] += 1
            else:
                rj[(x, y1)] = 1
##for i in range(10):
##    for j in range(10):
##        if (i, j) in rj:
##            print(rj[(i, j)], end = ' ')
##        else:
##            print('.', end = ' ')
##    print()
print(len(rj)-sum(map((1).__eq__, rj.values())))
