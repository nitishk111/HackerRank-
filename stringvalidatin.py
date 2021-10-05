if __name__ == '__main__':
    s = input()
    #print(s.isalnum())
    #print(s.isalpha())
    al,digit,lx,uc=0,0,0,0
    for i in s:
        if i.isalpha():
            al+=1
        if i.isdigit():
            digit+=1
        if i.islower():
            lx+=1
        if i.isupper():
            uc+=1
    print(al!=0 and digit!=0)
    print(al!=0)
    print(digit!=0)
    print(lx!=0)
    print(uc!=0)
