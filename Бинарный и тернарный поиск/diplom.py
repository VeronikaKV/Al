fin = open('input.txt', 'r')
spd, V, n = map(float, fin.readline().split())
n = int(n)
troiki = []
for i in range(n):
    troiki.append([j for j in map(float, fin.readline().split())])
fin.close()
S_all = 0
h_all = 0 #Right
for i in range(n):
    S_all += troiki[i][2] ** 2
    if troiki[i][1] + troiki[i][2] > h_all:
        h_all = troiki[i][1] + troiki[i][2]
h_all += 1
spd_all = S_all * spd

fout = open('output.txt', 'w')
if V - spd_all> 0.0000000001:
    print(-1, file = fout)
    quit()
bottom = 0 #Left
while h_all - bottom > 0.0000000001:
    mid = (h_all + bottom)/2
    S_wodaVKletke = 0
    for i in range(n):
        y, a = troiki[i][1], troiki[i][2]
        if mid > y:
            S_wodaVKletke += min(mid - y, a) * a
    if V - S_wodaVKletke * spd > 0.0000000001:
        bottom = mid
    else:
        h_all = mid
print(bottom, file = fout)
