ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
l_susjeda = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i != j:
            l_susjeda.append((i, j))
rj = dict()
for i in range(len(sve)):
    for j in range(len(sve[i]) - 1):
        rj[(i, j)] = int(sve[i][j])
risk = 0
for i in range(len(sve)):
    for j in range(len(sve[i]) - 1):
        uvjet = True
        for susjed in l_susjeda:
            if (i + susjed[0], j + susjed[1]) in rj:
                if rj[(i, j)] >= rj[(i + susjed[0], j + susjed[1])]:
                    uvjet = False
                    break
        if uvjet:
            risk += rj[(i, j)] + 1
print(risk)
        
    
    
