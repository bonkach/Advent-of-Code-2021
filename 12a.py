ulaz = open('ulaztest.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
put = dict()
for red in sve:
    a, b = list(map(str, red.strip().split('-')))
    if a in put:
        put[a].append(b)
    else:
        put[a] = [b]
    if b in put:
        put[b].append(a)
    else:
        put[b] = [a]
trenutni = 'start'
bili = ['start']
path = ['start']
while trenutni != 'end':
    for p in put[trenutni]:
        if p.islower() and p not in bili:
            trenutni = p
            bili.append(p)
            path.append(p)
            break
        elif p.isupper():
            trenutni = p
            path.append(p)
            break
print(path)    
