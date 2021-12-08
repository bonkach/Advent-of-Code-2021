ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
b = 0
prethodna_tri = sum(list(map(int,sve[:3])))
sve = sve[1:]
while len(sve) >= 3:
    nova_tri = sum(list(map(int,sve[:3])))
    if nova_tri > prethodna_tri:
        b += 1
    prethodna_tri = nova_tri
    sve = sve[1:]
print(b)
    
