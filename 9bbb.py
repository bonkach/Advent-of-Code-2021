from random import *
def susjedi(rj, x, y):
    l = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i, y + j) in rj and abs(i - j) == 1:
                l.append((x + i, y + j))
    return l
ulaz = open('ulaztest.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
rj = dict()
for i in range(len(sve)):
    for j in range(len(sve[i].strip())):
        if int(sve[i][j]) != 9:
            rj[(i, j)] = int(sve[i][j])
rj_pr = dict()
for i, j in rj.keys():
    rj_pr[(i, j)] = susjedi(rj, i, j)
while len(rj) > 0:
    pr = sorted(rj.keys())[0]
    del(rj[pr])
    bili = [pr] + rj_pr[pr]
    lista = rj_pr[pr]
    while len(bili) > 0:
        lista.extend(rj_pr[bili[0]])
        lista = list(set(lista))
        bili = bili[1:]
    for l in lista:
        if l in rj:
            del(rj[l])
