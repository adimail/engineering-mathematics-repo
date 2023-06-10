import math

def r2d(num):
    return num*math.pi/180

a=math.sin(r2d(90))
b=math.cos(r2d(84))

x=[0,30,60,90,120,150]
y=[0,902,19.6,17.8,17.3,11.7]

tblrow=[6][5]

for i in range(0,6):
    tblrow[i][0] = y[i]*math.sin(r2d(x[i]))
    tblrow[i][1] = y[i]*math.sin(r2d(2*x[i]))
    tblrow[i][2] = y[i]*math.cos(r2d(x[i]))
    tblrow[i][3] = y[i]*math.cos(r2d(2*x[i])) 

rows, cols = (6, 6)
tbl = [[0]*cols]*rows

print()

for i in tbl:
    for j in i:
        print(j,end="\t")
    print()
