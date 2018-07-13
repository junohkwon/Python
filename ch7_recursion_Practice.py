def f2(n):
    #baseline
    if n == 1:
        return n
    #recursive call
    else:
        if n%2==0:
            return 1 + f2(n//2)
        else:
            return 1 + f2(3*n+1)

# f2(1)
# f2(6)
# f2(11)
# f2(637228127)

def f4(lst):
    #baseline
    if lst == []:
        return
    else:
        #recursive call
        if lst[0]%2 == 1:
            print(lst[0]*3)
            return f4(lst[1:])
        else:
            return f4(lst[1:])

# f4([1,2,3,4])
# f4([2,4])
# f4([11,42,63,15])

def f6(lst):
    #baseline
    if lst == [] or type(lst) != list:
        return lst
    else:
        #recursive call
        if type(lst[0]) != list:
            return [lst[0]] + f6(lst[1:])
        else:
            return f6(lst[0]) + f6(lst[1:])

# f6(['baa'])
# f6(['baa',[4,True,[10,5],[1,2,['moo']]],['chirp']])
# f6([])
# f6([[[[[[[[[[[23]]]]]]]]]]])

def f8(s):
    if s =='' or len(s)==1:
        return True
    if s[0] != s[len(s)-1] :
        return False
    else:
        return f8(s[1:len(s)-1])

# f8('')
# f8('kayak')
# f8('penguin')
# f8('a')

def f10(lst):
    #baseline
    if lst == []:
        return 0
    else:
        # recursive call
        return 1 + f10(lst[1:])

# f10([1,2,3])
# f10([])
# f10([2])

def f12(n):
    if n == 0:
        return
    else:
        print(n)
        return f12(n-1)

# f12(3)
# f12(0)
# f12(1)

def f14(lst):
    #baseline1
    if lst == []:
        return None
    # baseline2
    if lst[0]%2 == 1:
        return lst[0]
    # recursive call
    else:
        return f14(lst[1:])

# f14([1,2,3])
# f14([2,4])
# f14([2,4,6,8,10,3])

def f16(lst):
    if lst == []:
        return lst
    else:
        if lst[0]%2 ==1:
            return [lst[0]] + f16(lst[1:])
        else:
            return f16(lst[1:])

# f16([1,3,5,7])
# f16([2,4])
# f16([1,2,3,4,5])

def f18(a,b):
    if b == 0:
        return a
    else:
        return f18(b,a%b)

# f18(5,4)
# f18(40,60)
# f18(9,3)