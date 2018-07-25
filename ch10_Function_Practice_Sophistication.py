def f2(lst):
    print(*list(filter(lambda x : x%2 == 1, lst)),sep='\n')

def f4(lst):
    return sum(list(map(lambda x : x[0] if x[1]%2==1 else 0,enumerate(lst))))

def f6(lst):
    return max(lst)

def f8(a,b,n):
    print(*(filter(lambda x : x%n==0, range(a,b+1))),sep='\n')

def f10(n):
    print(*(map(lambda x : '*'*x, range(1,n+1))),sep='\n')

def f12(lst):
    return all(map(lambda x : x < 0, lst))

def f14(lst):
    return list(filter(lambda x:x[1]<0, enumerate(lst)))[-1][0]

def f16(n):
    print(*(map(lambda x : '*'*x, range(n,0,-1))),sep='\n')

def f18(n):
    import math
    return math.factorial(n)

def f20(matrix):
    print(*list(map(lambda x:x[1][x[0]], enumerate(matrix))),sep='\n')

def f22(lst):
    li = list(map(lambda x:list(range(x,-1,-1)),lst))
    for i in li:
        print(*i)

def f24(n):
    print(*filter(lambda x : x%2==0 or x%3==0, range(1,n+1)),sep='\n')

def f26(lst):
    return sorted(lst)[-2]

def f28(lst):
    print(*map(lambda x : sorted(x[1])[-1], enumerate(lst)),sep='\n')
