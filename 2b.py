ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
g = ''
gamma = [0] * 5
for red in sve:
    red = red.strip()
    for i in range(len(red)):
        gamma[i] += int(red[i])
for i in range(5):
    if gamma[i] > len(sve) // 2:
        g += '1'
    else:
        g += '0'
e = g.replace('0','*').replace('1', '0').replace('*', '1')
print(int(e,2)*int(g,2))

