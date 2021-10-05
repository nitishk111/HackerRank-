

n,k=tuple(map(int,input().split()))
l=list(map(int,input().split()))
pro=l[len(l)-1]
j=len(l)-1
while j>=0:
    i=j-1
    while l[j]-l[i]<=k and i>=0:
        i-=1
    pro=pro*l[i+1]
    j=i-1
        

print(pro)
        
