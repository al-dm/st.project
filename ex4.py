import math
points = []
lines = []
n=int(input("Введите N:"))
for i in range(1,n+1):
    points.append((float(input("x"+str(i)+":")), float(input("y"+str(i)+":"))))
P=((points[n-1][0]-points[0][0])**2+(points[n-1][1]-points[0][1])**2)**0.5
S=points[n-1][0]*points[0][1]-points[0][0]*points[n-1][1]
for i in range(0,n-1):
 P+=((points[i][0]-points[i+1][0])**2+(points[i][1]-points[i+1][1])**2)**0.5


 S+=points[i][0]*points[i+1][1]
 S-=points[i+1][0]*points[i][1]
  #направляющие вектора прямых
 lines.append((points[i+1][0]-points[i][0],points[i+1][1]-points[i][1]))
lines.append((points[0][0]-points[n-1][0], points[0][1]-points[n-1][1]))


print("P=",P)
print("S=",0.5*abs(S))

if(points[n-1][0]*points[0][1]+points[1][0]*points[n-1][1]+points[0][0]*points[1][1]-points[1][0]*points[0][1]-points[n-1][1]*points[0][0]-points[n-1][0]*points[1][1])<0:#определитель матрицы для определения углов больше 180 градусов
 print("Угол у вершины 1 = ",math.degrees(math.acos(-(lines[n-1][0]*lines[0][0]+lines[n-1][1]*lines[0][1])/(((lines[n-1][0]**2+lines[n-1][1]**2)**0.5)*(lines[0][0]**2+lines[0][1]**2)**0.5))),"градусов")
else: print("Угол у вершины 1 = ",180+
math.degrees(math.acos((lines[n-1][0]*lines[0][0]+lines[n-1][1]*lines[0][1])/(((lines[n-1][0]**2+lines[n-1][1]**2)**0.5)*(lines[0][0]**2+lines[0][1]**2)**0.5))),"градусов")

for i in range(2,n):
    if(points[i-2][0]*points[i-1][1]+points[i][0]*points[i-2][1]+points[i-1][0]*points[i][1]-points[i][0]*points[i-1][1]-points[i-2][1]*points[i-1][0]-points[i-2][0]*points[i][1])<0:#определитель матрицы для определения углов больше 180 градусов
     print("Угол у вершины "+str(i)+" = ",math.degrees(math.acos(-(lines[i-2][0]*lines[i-1][0]+lines[i-2][1]*lines[i-1][1])/(((lines[i-2][0]**2+lines[i-2][1]**2)**0.5)*(lines[i-1][0]**2+lines[i-1][1]**2)**0.5))),"градусов")
    else: print("Угол у вершины "+str(i)+" = ",180+math.degrees(math.acos((lines[i-2][0]*lines[i-1][0]+lines[i-2][1]*lines[i-1][1])/(((lines[i-2][0]**2+lines[i-2][1]**2)**0.5)*(lines[i-1][0]**2+lines[i-1][1]**2)**0.5))),"градусов")
if(points[n-2][0]*points[n-1][1]+points[0][0]*points[n-2][1]+points[n-1][0]*points[0][1]-points[0][0]*points[n-1][1]-points[n-2][1]*points[n-1][0]-points[n-2][0]*points[0][1])<0:#определитель матрицы для определения углов больше 180 градусов
     print("Угол у вершины "+str(n)+" = ",math.degrees(math.acos(-(lines[n-2][0]*lines[n-1][0]+lines[n-2][1]*lines[n-1][1])/(((lines[n-2][0]**2+lines[n-2][1]**2)**0.5)*(lines[n-1][0]**2+lines[n-1][1]**2)**0.5))),"градусов")

else: print("Угол у вершины "+str(n)+" = ",180+math.degrees(math.acos((lines[n-2][0]*lines[n-1][0]+lines[n-2][1]*lines[n-1][1])/(((lines[n-2][0]**2+lines[n-2][1]**2)**0.5)*(lines[n-1][0]**2+lines[n-1][1]**2)**0.5))),"градусов")
    
