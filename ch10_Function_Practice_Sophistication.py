# def f2(lst):
#     print(*list(filter(lambda x : x%2 == 1, lst)),sep='\n')
#
# a = [1,2,3,4]
# b=[1,2,3,4,5]
# f2(a)
# f2(b)

# def f4(lst):
#     print(sum(list(map(lambda x : x[0] if x[1]%2==1 else 0,enumerate(lst)))))
#
# f4([1,2,3,4])
# f4([1,2,3,4,5])

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

# def f10(n):
#     print(*(map(lambda x : '*'*x, range(1,n+1))),sep='\n')
#
# f10(1)
# f10(2)
# f10(3)

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

# def f16(n):
#     print(*(map(lambda x : '*'*x, range(n,0,-1))),sep='\n')
#
# f16(3)
# f16(2)
# f16(1)

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

# def f22(lst):
#     print(*list(map(lambda x:list(range(x,-1,-1)),lst)),sep='\n')
#
# f22([1,3,5])

# def f24(n):
#     print(*filter(lambda x : x%2==0 or x%3==0, range(1,n+1)),sep='\n')
#
# f24(10)
# f24(1)
# f24(3)

# def f26(lst):
#     print(sorted(lst)[-2])
#
# f26([1,4,3,2,5])
# f26([3,2])
# f26([3,4])

# def f28(lst):
#     print(*map(lambda x : sorted(x[1])[-1], enumerate(lst)),sep='\n')
#
# f28([[1,2,3],[4,5,6],[7,8,9]])
# f28([[3,2,1],[0,-1,-2]])
# f28([[1,2,3,4],[1],[34],[2],[3],[56],[67]])