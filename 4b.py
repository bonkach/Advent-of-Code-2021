import copy
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
bingo = list(map(int, sve[0].split(',')))
rj = dict()
k = -1
for red in sve[1:]:
    if red == '\n':
        k += 1
        rj[k] = dict()
        i = j = 0
    else:
        red = list(map(int, red.split()))
        for i in range(5):
            rj[k][i, j] = red[i]
        j += 1
rj1 = [[0,0,0,0,0] for i in range(len(rj))]
rj2 = [[0,0,0,0,0] for i in range(len(rj))]
uvjet = False
rj3 = copy.deepcopy(rj)
pobj = set()
uvjet = False
for zn in bingo:
    for k in rj:
        for koo in rj[k]:
            if zn == rj[k][koo]:
                del(rj3[k][koo])
                rj1[k][koo[0]] += 1
                rj2[k][koo[1]] += 1
                if rj1[k][koo[0]] == 5:
                    pobj.add(k)
                elif rj2[k][koo[1]] == 5:
                    pobj.add(k)
                if len(pobj) == 100:
                    print(sum(rj3[k].values())*zn)
                    uvjet = True
                    break
            if uvjet:
                break
        if uvjet:
            break
    if uvjet:
        break

    
