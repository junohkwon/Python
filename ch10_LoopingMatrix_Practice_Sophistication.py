def f2(n):
    print(*map(lambda x : list(map(lambda k:k,range(x,2*x))), range(1,n+1)),sep='\n')

f2(3)

# 1
# ->
# 2
# ->3
# 4
# ->5,6


# def f6(matrix):
#     print(list(map(lambda x : sum(x), matrix)))
#
# f6([[1,0],[0,1]])

# def f8(matrix):
#     for i in range(0, len(matrix)):
#         print(*list(filter(lambda x:x%2==1, matrix[i])),sep=' ')
#
# f8([[1,0],[0,1]])