def f2(n):
    sum=1;
    for i in range(1,n+1):
        print(*list(map(lambda x:x, range(sum,sum+i))))
        sum += i


def f4(n):
    sum=1;
    for loop in range(0,2):
        for i in range(1,n+1):
            if(loop == 0):
                print(*list(map(lambda x: x, range(sum, sum + i))))
                sum += i
            else:
                print(*list(map(lambda x: x, range(sum, sum + (n-i)))))
                sum += (n-i)

def f6(matrix):
    return sum(list(map(lambda x : sum(x), matrix)))

def f8(matrix):
    for i in range(0, len(matrix)):
        print(*list(filter(lambda x:x%2==1, matrix[i])),sep=' ')

def f10(matrix1, matrix2):
    rmatrix=[]
    if len(matrix1[0]) == len(matrix2):
        for row in range(0,len(matrix1)):
            lst=[]
            value=0
            for col2 in range(0, len(matrix2[0])):
                lst.append(sum(list(map(lambda col : matrix1[row][col]*matrix2[col][col2], range(0, len(matrix1[row]))))))
            rmatrix.append(lst)
    return rmatrix

def f12(rows, cols):
    matrix=[]

    for r in range(0,rows):
        row=[]
        for c in range(0,cols):
            cal=0
            if r-1 >= 0:
                cal+=1
            if r+1 < rows:
                cal += 1
            if c-1 >= 0:
                cal += 1
            if c+1 < cols:
                cal += 1
            row.append(cal)
        matrix.append(row)

    return matrix