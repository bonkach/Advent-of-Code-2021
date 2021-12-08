from statistics import median
ulaz = open('ulaz.txt', 'r')
sve = list(map(int, ulaz.read().split(',')))
ulaz.close()
med = int(median(sve))
ars = round(sum(sve)/len(sve))
l = []
for i in range(min(med, ars), max(med, ars) + 1):
    br = 0
    for krab in sve:
        raz = abs(krab - i)
##        for j in range(raz + 1):
##            zbr += j
        zbr = raz * (raz + 1) / 2 #gauss
        br += zbr
    l.append(br)
print(int(min(l)))
    
