def check_vowel(s):
    l=["A","I","O","E","U"]
    if s in l:
        return 1
    return 0
def minion_game(string):
    # your code goes here
    sub=[string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
    d=dict()
    for i in sub:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    del sub
    del string
    s=0
    k=0
    for i in d.keys():
        if check_vowel(i[0])==1:
            k=k+d[i]
        else:
            s=s+d[i]
    print(sub,'\n',d)
    if s>k:
        print('Sturt',s,k)
    elif s<k:
        print('Kevin',k,s)
    else:
        print('DRAW')


if __name__ == '__main__':
    s = input()
    print(len(s))
    minion_game("banana")
