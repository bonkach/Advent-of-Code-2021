ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
b = 0
prethodni = int(sve[0])
for red in sve[1:]:
    if int(red) > prethodni:
        b += 1
    prethodni = int(red)
print(b)

    
