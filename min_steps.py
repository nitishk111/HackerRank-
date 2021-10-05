
def steps(a,b,n):
    if a>b:
        a=a-b
        if a%2==0:
            return int(a/2)
        else:
            return int((a//2)+1)
    else:
        c=0
        if b>a*n:
            while b>a*n:
                a=a*n
                c+=1
        a=b-a
        if a%2==0:
            return int((a/2)+c)
        else:
            return int((a//2)+1+c)

l1=list()
l2=list()
t=int(input())
for i in range(t):
    l1=list(map(int,input().split()))
    l2.append(l1)

i=0
while i<t:
    s=steps(l2[i][0],l2[i][1],l2[i][2])
    print(s)
    i+=1
