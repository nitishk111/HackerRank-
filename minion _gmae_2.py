
def check_vowel(s):
    l=['A','E','I','O','U']
    if s in l:
        return 1
    return 0

def sub_string(string):
    global sub
    sub=[string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]

def minion_game(string):
    # your code goes here
    global sub
    global d
    d=dict()
    j=len(string)-1
    if j>999:
        j=999
    i=int()
    i=0
    print(type(i),type(j),type(len(string)-1))
    c=int(len(string)-1)
    while i<c:
        sub_string(string[i:j])
        i=j
        
        

        for i in sub:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
    s=0
    k=0
    for i in d.keys():
        if check_vowel(i[0])==1:
            k=k+d[i]
        else:
            s=s+d[i]
    if s>k:
        print('Stuart',s)
    elif s<k:
        print('Kevin',k)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
