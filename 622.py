n=int(input())
L=[]
while n>0:
    a=n%2
    L.append(a)
    n=n//2
A=L.count(1)
print(A)