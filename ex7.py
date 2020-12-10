import sys
k=int(input("Введите основание степени счиления: "))
K=k
num = input("Введите число: ")
m= int(input("Введите делитель: "))
f=1
s=0
n= len(num)
for i in range(0,n):
    j=ord(num[n-i-1])
    if j<58 :
        if j-48<K:
            s+=f*(j-48)
        else: 
            print("Ошибка: введённое число не по основанию",K)
            sys.exit(0)
    else:
        if j-55<K:
            s+=f*(j-55)
        else: 
            print("Ошибка: введённое число не по основанию",K)
            sys.exit(0)

    f*=k
print("Остаток при делении =",str(s%m))

