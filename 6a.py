from collections import *
ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
sve = list(map(int, sve.split(',')))
ulaz.close()
dani = 80
for k in range(dani):
    sve = list(map(lambda x: x - 1, sve))
    while -1 in sve:
        sve[sve.index(-1)] = 6
        sve.append(8)
print(len(sve))
        
        
