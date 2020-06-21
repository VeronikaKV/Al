f=open('diploma.in', 'r').read().split(' ')
xr=1
while (((xr // int(f[0])) * (xr // int(f[1]))) < int(f[2])): 
    xr = xr * 2
xl = xr // 2
while (xr - xl > 1):
    if (((((xr - xl) // 2) + xl) // int(f[0])) * ((((xr - xl) // 2) + xl) // int(f[1])) < int(f[2])) :  xl = ((xr - xl) // 2) + xl
    else: xr = ((xr - xl) // 2) + xl

h=open('diploma.out', 'w')
h.write(str(xr))