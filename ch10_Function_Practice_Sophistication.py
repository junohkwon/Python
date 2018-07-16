# def f2(lst):
#     print(*list(filter(lambda x : x%2 == 1, lst)),sep='\n')
#
# a = [1,2,3,4]
# b=[1,2,3,4,5]
# f2(a)
# f2(b)

# def f4(lst):
#      pass

# def f6(lst):
#     print(max(lst))
#
# f6(a)
# f6(b)

# def f8(a,b,n):
#     print(*(filter(lambda x : x%n==0, range(a,b+1))),sep='\n')
#
# f8(1,10,2)
# f8(1,10,11)
# f8(1,10,7)

# def f12(lst):
#     print(all(map(lambda x : x < 0, lst)))
#
# f12([])
# f12([-1,-2,-3,-4,5])
# f12([1,2,3,4,5])
# f12([-1,-2,-3])

# def f14(lst):
#     return list(filter(lambda x:x[1]<0, enumerate(lst)))[-1][0]
#
# a=[1,2,-3]
# b=[1,-2,-3,1,-2,-3]
# c=[-1,1,1,1]
# f14(a)
# f14(b)
# f14(c)

# import math
# def f18(n):
#     return math.factorial(n)
#
# f18(0)
# f18(2)
# f18(3)

# def f20(matrix):
#     #print(*list(map(lambda x:x[1][x[0]], enumerate(matrix))),sep='\n')
#     pass
#
# #enumerate(matrix) ==> [(0,[1,2,3]),(1,[4,5,6]),(2,[7,8,9])]
# #x[1] = x[x[0]]
#
# # lambda x:matrix[x][x], range(matrix)
#
# f20([[1,2,3],[4,5,6],[7,8,9]])

def f22(lst):
    print(*list(map(lambda x:list(range(x,-1,-1)),lst)),sep='\n')

f22([1,3,5])