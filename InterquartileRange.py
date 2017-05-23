import numpy as np
n=input()
X=list(map(int,input().split()))
F=list(map(int,input().split()))
S=[]
for i in range(len(X)):
     S=S+([X[i]]*F[i])

S.sort()
def median(x):
    n=len(x)
    if n%2==0:
        median=(x[n//2-1]+x[n//2])*1.0/2
    else:
        median = x[n//2]
    return median

L=S[:len(S)//2]
U=S[len(S)//2+1:]
print('%.1f' %(median(U)-median(L)))
