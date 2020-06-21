import math
f=open('input.txt', 'r').read().split()
x=1/3
xr=1
xl=0
x2=2*x
while x2-x>(10e-9):
    if ( ((1-float(f[2]))**2)+x**2 )**0.5 / float(f[0] ) +( ((1-x)**2) + float(f[2])**2 )**0.5 / float(f[1]) < \
       ( ((1-float(f[2]))**2)+x2**2 )**0.5 / float(f[0] ) +(( ((1-x2)**2)+float(f[2])**2 )**0.5 / float(f[1])):
       xr=x2
       x=(xr-xl)/3
       x2=(xr-xl)/3*2
    else: 
        xl=x
        x=(xr-xl)/3+xl
        x2=xr-(xr-xl)/3
h=open('output.txt', 'w')
h.write(str(xr))