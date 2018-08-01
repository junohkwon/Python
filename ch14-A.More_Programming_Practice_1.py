def first_perfect_square(lst):
    l = list(enumerate(lst))
    if l == [] or l[0][1] < 0:
        return -1
    else:
        temp = int(l[0][1]**0.5)
        if temp**2 == l[0][1]:
            return l[0][0]
        else:
            return first_perfect_square(lst[1:])

print(first_perfect_square([2,4,6,8,10,12]))
print(first_perfect_square([42]))


def first_perfect_square(numbers):
    for i in range(0, len(numbers)):
        if numbers[i] >= 0:
            if numbers[i]**0.5 - int(numbers[i]**0.5) == 0:
                return i
    return -1


def num_perfect_squares(numbers):
    cnt=0
    for i in range(0, len(numbers)):
        if numbers[i] >= 0:
            if numbers[i]**0.5 - int(numbers[i]**0.5) == 0:
                cnt += 1
    return cnt

print(num_perfect_squares([4]*10))

def second_largest(values):
    max=values[0]
    smax=values[0]
    for val in values:
        if val > max:
            smax = max
            max = val
        elif val > smax:
            smax = val

    return smax

print(second_largest([3,-2,10,-1,5]))
print(second_largest([-2,1,1,-3,5]))
print(second_largest(['alpha','gamma','beta','delta']))
print(second_largest([True,False,False,True]))
print(second_largest([3.1,3.1]))


