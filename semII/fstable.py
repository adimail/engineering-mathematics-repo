import math

def r2d(num):
    return num*math.pi/180

a=math.sin(r2d(90))
b=math.cos(r2d(84))

x=[0,30,60,90,120,150]
y=[0,09.2,14.6,17.8,17.3,11.7]

tblrow=[]
rows, cols=6,6

tblrow = [ [0 for i in range(cols)] for j in range(rows)]

for i in range(rows):
    tblrow[i][0]=x[i]
    tblrow[i][1]=y[i]

for r in range(len(tblrow)):
    for c in range(len(tblrow[r])):
        tblrow[r][2] = y[r]*math.sin(r2d(x[r]))
        tblrow[r][3] = y[r]*math.sin(r2d(2*x[r]))
        tblrow[r][4] = y[r]*math.cos(r2d(x[r]))
        tblrow[r][5] = y[r]*math.cos(r2d(2*x[r]))


for i in tblrow:
    for j in i:
        print(round(j,2),end="\t\t")
    print("\n")