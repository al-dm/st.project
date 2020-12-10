def det_1(i,j):
   if data[i][0]*data[j][1]+data[3][0]*data[i][1]+data[j][0]*data[3][1]-data[3][0]*data[j][1]-data[j][0]*data[i][1]-data[i][0]*data[3][1]==0:
       return True
   else :
        return False
def det_2(i,j):
   if data[i][0]*data[j][1]+data[3][0]*data[i][1]+data[j][0]*data[3][1]-data[3][0]*data[j][1]-data[j][0]*data[i][1]-data[i][0]*data[3][1]>0:
       return True
   else :
        return False
data = []
with open("in.txt") as f:
    for line in f:
          data.append([float(x) for x in line.split((';'))])
f1=open("out.txt",'w') 
#принадлежит ли точка сторонам треугольника
if det_1(0,1):
    f1.write("Да\nДа")
else :
    if det_1(1,2):
     f1.write("Да\nДа")
    else :
        if det_1(2,0):
         f1.write("Да\nДа")
        else:
         f1.write("Нет\n")
         # принадлежит ли точка плоскости ограниченной треугольником
         if(det_2(0,1)==det_2(1,2)==det_2(2,0)):
              f1.write("Да")
         else:
               f1.write("Нет")
f1.close()


