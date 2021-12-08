def gama(sve, k):
    n = len(sve[0].strip())
    gamma = [0] * n
    for red in sve:
        red = red.strip()
        for i in range(len(red)):
            gamma[i] += int(red[i])
    if gamma[k] >= len(sve) - gamma[k]:
        return '1'
    else:
        return '0'
    
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
n = len(sve[0].strip())

ga = sve[:]
for i in range(n):
    g = gama(ga, i)
    gan = ga[:]
    for red in ga:
        if red[i] != g:
            gan.remove(red)
    ga = gan[:]
    if len(ga) == 1:
        break

ep = sve[:]
for i in range(n):
    if gama(ep, i) == '0':
        e = '1'
    else:
        e = '0'
    eps = ep[:]
    for red in ep:
        if red[i] != e:
            eps.remove(red)
    ep = eps[:]
    if len(ep) == 1:
        break
print(int(ga[0], 2) * int(ep[0], 2))
                
                
        

    
