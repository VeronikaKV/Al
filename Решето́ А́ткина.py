chislo = int(input())    # число, до которого хотим найти простые числа 
limit = [False for k in range(chislo+1)] 
x2, dx2 = 1, 3
for i in limit:
    y2, dy2 = 1, 3
    for j in limit:
        n = 4 * x2 + y2 # 
        if n <= chislo and (n%12 == 1 or n%12 == 5):
            limit[n] = True
        n -= x2  #n = 3 * x2 + y2; 
        if n <= chislo and n%12 == 7:
            limit[n] = True
        if (x2 > y2): 
            n -= 2 * y2 #n = 3 * x2 - y2;
            if n <= chislo and n%12 == 11:
                limit[n] = True
        y2 += dy2
        dy2 += 2
    x2 += dx2
    dx2 += 2
r = 5
r2, dr2 = r*r, r*2+1
#Отсеиваем кратные квадратам простых чисел в интервале
for r in range(5, chislo+1):
    if limit[r] == True: 
        for mr2 in range(r2, chislo+1, r2):
            limit[mr2] = False
    r2+=dr2
    dr2+=2
limit[2], limit[3] = True, True

h=open('output.txt', 'w')
for nam in range(2, chislo+1):
    if limit[nam] == True :
        h.write(str(nam)+"\n")

