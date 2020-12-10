from decimal import Decimal, getcontext
k=int(input("Введите k:"))
s=Decimal('0')
f=1
getcontext().prec = 50
for i in range(1,k+1):
    f*=i
    s+=Decimal(Decimal('1')/f)
print("s =",s)