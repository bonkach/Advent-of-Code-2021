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
    for j in range(len(sve[i]) - 1):
        if int(sve[i][j]) != 9:
            rj[(i, j)] = int(sve[i][j])
risk = 1
while len(rj) != 0:
    pr = [sorted(rj.keys())[0]]
    del(rj[sorted(rj.keys())[0]])
    bili = [sorted(rj.keys())[0]]
    while len(pr) > 0:
        for susjed in susjedi(rj, pr[0][0], pr[0][1]):
            if susjed not in pr:
                pr.append(susjed)
                del(rj[susjed])
        pr = pr[1:]
        print(pr)
    bili.extend(pr)
    print(pr, len(pr))
    risk *= len(pr)
print(risk)
        
    
    
