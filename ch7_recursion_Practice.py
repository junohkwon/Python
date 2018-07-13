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

def f6(lst):
    #baseline
    if lst == [] or type(lst) != list:
        return lst
    else:
        if type(lst[0]) != list:
            return [lst[0]] + f6(lst[1:])
        else:
            return f6(lst[0]) + f6(lst[1:])

a = f6(['baa',[4,True,[10,5],[1,2,['moo']]],['chirp']])
print(a)


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
