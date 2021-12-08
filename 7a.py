ulaz = open('ulaz.txt', 'r')
sve = list(map(int, ulaz.read().split(',')))
ulaz.close()
krabba = dict()
for krab in sve:
    if krab not in krabba:
        krabba[krab] = 1
    else:
        krabba[krab] += 1
najv = max(krabba.values())
for key, val in krabba.items():
    if val == najv:
        najk = key
br = 0
for krab in sve:
    br += abs(krab - najk)
print(br)
    
