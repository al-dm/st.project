
N=int(input("Введите целое N>1:"))
num=int(N**0.5)
a=[]
for k in range(num+1):
    a.append(k)
a[1] = 0
i=2
print(N, end="=")
while i*i <= N:# a[i]<=sqrt(N)
   while N%i == 0:
        print(i, end = "")
        N =int(N/i)
        if N!=1:
           print("*", end = "")
   for j in range(i, num+1, i):
      a[j] = 0
   while i <= num and a[i]==0:
      i += 1
if N!=1:
  print(N)

