import math

def r2d(num):
    return num*math.pi/180

x=[0, 30, 60, 90, 120, 150]
#x=[0, 60, 120, 240, 300]

x = list(map(float, input().split()))
y = list(map(float, input().split()))

tblrow=[]
cols=6

tblrow = [ [0 for i in range(cols)] for j in range(6)]


for r in range(len(tblrow)):
    tblrow[r][0]=x[r]
    tblrow[r][1]=y[r]

    for c in range(len(tblrow[r])):
        tblrow[r][2] = y[r]*math.sin(r2d(x[r]))
        tblrow[r][3] = y[r]*math.sin(r2d(2*x[r]))
        tblrow[r][4] = y[r]*math.cos(r2d(x[r]))
        tblrow[r][5] = y[r]*math.cos(r2d(2*x[r]))


for i in tblrow:
    print("\n")
    for j in i:
        print(round(j,2),end="\t\t")