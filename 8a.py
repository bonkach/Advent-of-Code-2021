ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
br = 0
for red in sve:
    red = red.split('|')
    inp = red[0].split()
    out = red[1].split()
    signali = [set(x) for x in inp]
    zn = dict()
    for signal in signali:
        if len(signal) == 2:
            zn[1] = signal
        elif len(signal) == 3:
            zn[7] = signal
        elif len(signal) == 4:
            zn[4] = signal
        elif len(signal) == 7:
            zn[8] = signal
    del(signali[signali.index(zn[1])])
    del(signali[signali.index(zn[7])])
    del(signali[signali.index(zn[4])])
    del(signali[signali.index(zn[8])])
    nulajedandvatripet = zn[7] | zn[4]
    jedantri = zn[4] - zn[1]
    nula = zn[7] - zn[1]
    for signal in signali:
        if len(signal) == 6 and len(signal - nulajedandvatripet) == 1:
            šest = signal - nulajedandvatripet
            zn[9] = signal
    nulajedantrišest = nula | šest | jedantri
    del(signali[signali.index(zn[9])])
    for signal in signali:
        if len(signal) == 5 and len(signal - nulajedantrišest) == 1:
            pet = signal - nulajedantrišest
            zn[5] = signal
    del(signali[signali.index(zn[5])])
    for signal in signali:
        if len(signal) == 6 and len(signal - zn[5]) == 1:
            četiri = signal - zn[5]
            zn[6] = signal
    del(signali[signali.index(zn[6])])
    for signal in signali:
        if len(signal) == 6:
            zn[0] = signal
    del(signali[signali.index(zn[0])])
    for signal in signali:
        if četiri & signal:
            zn[2] = signal
    del(signali[signali.index(zn[2])])
    zn[3] = signali[0]
    broj = ''
    for signal in out:
        skup = set(signal)
        for k, v in zn.items():
            if skup == v:
                broj += str(k)
    br += int(broj)
print(br)            
