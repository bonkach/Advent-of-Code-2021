from statistics import median
ulaz = open('ulaz.txt', 'r')
sve = list(map(int, ulaz.read().split(',')))
ulaz.close()
med = int(median(sve))
br = 0
for krab in sve:
    br += abs(krab - med)
print(br)
    
