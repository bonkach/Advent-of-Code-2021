ulaz = open('ulaztest.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
br = 0
for red in sve:
    stog = []
    for znak in red.strip():
        if znak in '([{<':
            stog.append(znak)
        else:
            zadnji = stog.pop()
            if znak == ')' and zadnji != '(':
                br += 3
                break
            elif znak == ']' and zadnji != '[':
                br += 57
                break
            elif znak == '}' and zadnji != '{':
                br += 1197
                break
            elif znak == '>' and zadnji != '<':
                br += 25137
                break
print(br)
            
