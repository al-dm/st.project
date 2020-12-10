num=input("Введите двоичное число:")
n=len(num)
chet=nechet=0
s=[0,0,0,0]
i=n-1
while i>=0:
    if i%2==0:
        chet+=int(num[i])
    else:
     nechet+=int(num[i])
    s[(n-i-1)%4]+=int(num[i])
    i-=1
if abs(chet-nechet)%3==abs(s[0]-s[2]+2*(s[1]-s[3]))%5==0:
    print("Число делится на 15 без остатка")
else:
    print("Число не делится на 15 без остатка")
   