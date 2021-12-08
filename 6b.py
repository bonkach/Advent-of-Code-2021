ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
sve = list(map(int, sve.split(',')))
ulaz.close()
n = 80
l = []
br = len(sve)
for r in sve:
    prvi = r + 1
    ostali = [i for i in range(prvi, n + 1, 7)]
    l.append(ostali)
while len(l) != 0:
    for r in l[0]:
        ostali = []
        br += 1
        prvi = r + 9
        if prvi <= n:
            ostali = [i for i in range(prvi, n + 1, 7)]
        l.append(ostali)
    l = l[1:]
print(br)        
    
    
    
         
