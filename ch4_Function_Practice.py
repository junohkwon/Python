def f2(lst):
    for i in range(0,len(lst)):
        if lst[i] % 2 ==1:
            print(lst[i])

def f4(lst):
    sumval = 0
    for i in range(0,len(lst)):
        if lst[i] % 2 ==1:
            sumval += i
    return sumval

def f6(lst):
    maxval= lst[0]
    for i in range(0,len(lst)):
        if lst[i] > maxval:
            maxval = lst[i]
    return maxval

def f8(a,b,n):
    for i in range(a,b+1):
        if i % n == 0:
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
