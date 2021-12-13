def susjedi(x, y):
    l = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                pass
            else:
                l.append((x + i, y + j))
    return l
ulaz = open('ulaztest.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
mat = dict()
for i in range(len(sve)):
    for j in range(len(sve[i].strip())):
        mat[i, j] = int(sve[i][j])
br = 0
for ž in range(196):
    for k in mat:
        mat[k] += 1
    while max(mat.values()) > 9:
        for k, v in mat.items():
            if v > 9:
                for susjed in susjedi(k[0], k[1]):
                    if susjed in mat:
                        if mat[susjed] != 0:
                            mat [susjed] += 1
                mat[k] = 0
                br += 1
    if ž == 195:
        for i in range(len(sve)):
            for j in range(len(sve[i].strip())):
                print(mat[i, j], end = '')
            print()
        print()
print(br)
