
n,k=tuple(map(int,input().split()))
l=[]
for i in range(n):
    l.append(int(input()))

c=0
for i in l:
    if i%k==0:
        c+=1
print(c)
    
