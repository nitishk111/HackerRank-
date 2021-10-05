def sub_strings(s):
    res=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    print(type(res))
    print(res)
    a=set(res)
    print(list(a))
    print(len(a),len(res))

sub_strings('mango')
            
