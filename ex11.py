import time
import sys
start_time = time.time()
prime = []
def pre(A,n,i):
    while i < A:
        if a[i] != 0:
            prime.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return i
 
def post(n,i):
    while i <= n:
        if a[i]!= 0:
            fout.write(str(a[i])+"\n")
            prime.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1

fin = open('in.txt', 'r')
A=int(fin.readline())
B=int(fin.readline())
a=[]
for k in range(B+1):
    a.append(k)
a[1] = 0
fout = open('out.txt', 'w')
if A>B:
    print("Error:A>B")
    sys.exit(0)
i=2
if(A>2):
    post(B,pre(A,B,i))
else:
 post(B,i)
fout.close()

print("--- %s seconds ---" % (time.time() - start_time))

