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
l_koo = []
for i in range(len(sve)):
    for j in range(len(sve[i]) - 1):
        if int(sve[i][j]) != 9:
            rj[(i, j)] = int(sve[i][j])
risk = 1
bili = []
while len(rj) != 0:
    pr = [sorted(rj.keys())[0]]
    del(rj[sorted(rj.keys())[0]])
    for i in range(len(sve)):
        for j in range(len(sve[i]) - 1):
            for koo in pr:
                if (i, j) in susjedi(rj, koo[0], koo[1]) and (i,j) not in pr and (i, j) not in bili: 
                    pr.append((i, j))
                    del(rj[(i, j)])
                    bili.append((i, j))
    print(pr, len(pr))
    risk *= len(pr)
print(risk)
        
    
    
