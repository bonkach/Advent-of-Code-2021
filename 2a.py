ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
poz = [0,0]
for red in sve:
    red = red.split()
    smjer = red[0]
    kol = int(red[1])
    if smjer == 'forward':
        poz[0] += kol
    elif smjer == 'down':
        poz[1] += kol
    else:
        poz[1] -= kol
print(poz[0] * poz[1])
