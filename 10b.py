ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
dobre = []
l_br = []
for red in sve:
    stog = []
    uvjet = True
    for znak in red.strip():
        if znak in '([{<':
            stog.append(znak)
        else:
            zadnji = stog.pop()
            if znak == ')' and zadnji != '(':
                uvjet = False
                break
            elif znak == ']' and zadnji != '[':
                uvjet = False
                break
            elif znak == '}' and zadnji != '{':
                uvjet = False
                break
            elif znak == '>' and zadnji != '<':
                uvjet = False
                break
    if uvjet:
        br = 0
        while len(stog) > 0:
            br *= 5
            zadnji = stog.pop()
            if zadnji == '(':
                br += 1
            elif zadnji == '[':
                br += 2
            elif zadnji == '{':
                br += 3
            else:
                br += 4
        l_br.append(br)
l_br.sort()
print(l_br[len(l_br)//2])
