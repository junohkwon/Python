'''
ch0. Homework
Function Practice
'''

def f2(lst):
    for i in range(0,len(lst)):
        if lst[i] % 2 ==1:
            print(lst[i])

def f2_new(lst):
    for x in filter(lambda x : x%2, lst):
        print(x)


def f4(lst):
    sumval = 0
    for i in range(0,len(lst)):
        if lst[i] % 2 ==1:
            sumval += i
    return sumval

from functools import reduce
def f4_new(lst):
    newlst = list(filter(lambda x : x%2, lst))
    return reduce(lambda x,y:x+y, newlst)


def f6(lst):
    maxval= lst[0]
    for i in range(0,len(lst)):
        if lst[i] > maxval:
            maxval = lst[i]
    return maxval

def f6_new(lst):
    return max(lst)


def f8(a,b,n):
    for i in range(a,b+1):
        if i % n == 0:
            print(i)

def f8_new(a,b,n):
    for i in filter(lambda x:x%n == 0, range(a,b+1)):
        print(i)


def f10(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print('*',end='')
        print()

def f12(lst):
    negative_cnt = 0
    for i in range(0,len(lst)):
        if lst[i] < 0:
            negative_cnt += 1

    if negative_cnt == len(lst):
        return True
    else:
        return False

def f14(lst):
    max_idx=-1
    for i in range(0,len(lst)):
        if lst[i] < 0:
            max_idx = i

    return max_idx

def f16(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print('*',end='')
        print()

def f18(n):
    fac = 1
    for i in range(n,0,-1):
        fac = fac * i

    return fac

def f20(lst):
    for row in range(0,len(lst)):
        for i in range(lst[row],-1,-1):
            print(i,end=' ')
        print()

def f22(n):
    for i in range(1,n+1):
        if i%2 == 0 or i%3 == 0:
            print(i)

def f24(lst):
    fir_max= -99999
    sec_max= -99999

    for val in lst:
        if val > fir_max:
            sec_max = fir_max
            fir_max = val

        elif val > sec_max:
            sec_max = val
    return sec_max

def f26(lst):
    for row in range(0,len(lst)):
        maxval = lst[row][0]
        for col in range(0, len(lst[row])):
            if lst[row][col] > maxval:
                maxval = lst[row][col]

        print(maxval)

print('====== f2 ======')
f2([1,2,3,4])
f2([1,2,3,4,5])

print('====== f4 ======')
print(f4([1,2,3,4]))
print(f4([1,2,3,4,5]))

print('====== f6 ======')
print(f6([1,2,3,4]))
print(f6([1,2,3,4,5]))

print('====== f8 ======')
f8(1,10,2)
f8(1,10,11)
f8(1,10,7)

print('====== f10 ======')
f10(1)
f10(2)
f10(3)

print('====== f12 ======')
print(f12([]))
print(f12([-1,-2,-3,-4,5]))
print(f12([1,2,3,4,5]))
print(f12([-1,-2,-3]))

print('====== f14 ======')
print(f14([1,2,-3]))
print(f14([1,-2,-3,1,-2,-3]))
print(f14([-1,1,1,1]))

print('====== f16 ======')
f16(3)
f16(2)
f16(1)

print('====== f18 ======')
print(f18(0))
print(f18(2))
print(f18(3))

print('====== f20 ======')
f20([])
f20([1,3,5])
f20([5,3,6,2])

print('====== f22 ======')
f22(10)
f22(1)
f22(3)

print('====== f24 ======')
print(f24([1,4,3,2,5]))
print(f24([3,2]))
print(f24([3,4]))

print('====== f26 ======')
f26([[1,2,3],[4,5,6],[7,8,9]])
f26([[3,2,1],[0,-1,-2]])
f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]])

