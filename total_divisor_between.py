
c=0
for i in range(1000,100001):
    if i%15==0 and i%35==0 and i%77==0:
        #print(i)
        c+=1
print(c)
