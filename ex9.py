import sys
x1=float(input("Введите кооридинаты первой точки х1:"))
x2=float(input("Введите кооридинаты первой точки x2:"))
y1=float(input("Введите кооридинаты второй точки y1:"))
y2=float(input("Введите кооридинаты второй точки y2:"))
z1=float(input("Введите кооридинаты третьей точки z1:"))
z2=float(input("Введите кооридинаты третьей точки z2:"))

if (x1==z1 and x2==z2) or (y1==z1 and y2==z2) or (x1==y1 and x2==y2):
    print("Некорректные входные данные")
    sys.exit(0)
#уравнение исходной прямой
if(x1-y1)!=0:
    a1=(x2-y2)/(x1-y1)
    b1=x2-a1*x1
else:
    x=x1
    y=z2

# уравнение нормальной прямой
if(y2-x2)!=0:
    a2=-(y1-x1)/(y2-x2)
    b2=z1*(y1-x1)/(y2-x2)+z2
else :
    x=z1
    y=x2

#координаты точки пересечения прямых
if(x1-y1)!=0 and (y2-x2)!=0:
    x=(b2-b1)/(a1-a2)  
    y=a1*x+b1

if (x1>y1):
    if(x<=x1 and x>=y1):
     print("Пересечение принадлежит отрезку")
    else:
     print("Пересечение принадлежит продолжению отрезка")
else:
    if(x1==y1):
        if (x2>y2):
             if(y<=x2 and y>=y2):
                 print("Пересечение принадлежит отрезку")
             else:
                print("Пересечение принадлежит продолжению отрезка")
        else:
            if(y>=x2 and y<=y2):
                 print("Пересечение принадлежит отрезку")
            else:
                print("Пересечение принадлежит продолжению отрезка")
    else:
        if(x>=x1 and x<=y1):
             print("Пересечение принадлежит отрезку")
        else:
            print("Пересечение принадлежит продолжению отрезка")
            


