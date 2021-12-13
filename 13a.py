ulaz = open('ulaztest.txt', 'r')
red = ulaz.readline()
koo = dict()
while len(red) > 2:
    x, y = map(int, red.strip().split(','))
    koo[x, y] = 1
    red = ulaz.readline()
fold = ulaz.readlines()
for red in fold:
    maxx = max(koo.keys(), key = lambda x: x[0])[0]
    maxy = max(koo.keys(), key = lambda x: x[1])[1]
    red = red.strip().split()
    os = red[2].split('=')[0]
    sekač = int(red[2].split('=')[1])
    if os == 'y':
        k = 0
        for i in range(maxy, sekač, -1):
            for j in range(maxx + 1):
                if (j, i) in koo:
                    koo[j, k] = 1
                    del(koo[j, i])
            k += 1
    else:
        k = 0
        for i in range(maxx, sekač, -1):
            for j in range(maxy + 1):
                if (i, j) in koo:
                    koo[k, j] = 1
                    del(koo[i, j])
            k += 1
    break
##maxx = max(koo.keys(), key = lambda x: x[0])[0]
##maxy = max(koo.keys(), key = lambda x: x[1])[1]
##for i in range(maxy + 1):
##    for j in range(maxx + 1):
##        if (j, i) in koo:
##            print('#', end = ' ')
##        else:
##            print('.', end = ' ')
##    print()
print(len(koo))           
            

            
        
