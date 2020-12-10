import copy
import sys
def razv(i,j,s, way,step):
    s+=A[i][j]
    if not i==j==0:
        way.append(step)
    global min_s
    global min_way
    #путь1
    if(j!=n-1):
     razv(i,j+1,s,copy.copy(way),1)
    #путь2
    if(i!=n-1):
        razv(i+1,j,s,copy.copy(way),0)
   # выход из рекурсии
    if(i==j==n-1):
        if(s<min_s):
            min_s=s
            for k in range(0,2*n-2):
                min_way[k]=way[k]
           

s=0
i=0
j=0
min_way=[]
way=[]
with open('in.txt') as f:
    A = [list(map(int, row.split())) for row in f.readlines()]
with open('in.txt') as f:
    n=int(len(f.readline())/2)
if n==0:
    print("Error:Введите таблицу NxN,N>1")
    sys.exit(0)
min_s=9*(2*n-2)
for k in range(0,2*n-2):
    min_way.append(0)
razv(0,0,s,way,0)
print("Общая сумма =",min_s, "Путь:", min_way,", где 1 - вправо, 0 - вниз")
