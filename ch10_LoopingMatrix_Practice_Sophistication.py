# def f2(n):
#     sum=1;
#     for i in range(1,n+1):
#         print(*list(map(lambda x:x, range(sum,sum+i))))
#         sum += i
#
# f2(3)
# f2(0)
# f2(5)

# def f4(n):
#     sum=1;
#     for loop in range(0,2):
#         for i in range(1,n+1):
#             if(loop == 0):
#                 print(*list(map(lambda x: x, range(sum, sum + i))))
#                 sum += i
#             else:
#                 print(*list(map(lambda x: x, range(sum, sum + (n-i)))))
#                 sum += (n-i)
#
# f4(3)
# f4(0)
# f4(1)


# def f6(matrix):
#     print(sum(list(map(lambda x : sum(x), matrix))))
#
# f6([[1,0],[0,1]])
# f6([[1,2,3],[4,5,6]])
# f6([[1],[2],[3],[4]])

# def f8(matrix):
#     for i in range(0, len(matrix)):
#         print(*list(filter(lambda x:x%2==1, matrix[i])),sep=' ')
#
# f8([[1,0],[0,1]])
# f8([[1,2,3],[4,5,6]])
# f8([[1],[2],[3],[4]])

def f10(matrix1, matrix2):
    pass