def f2(n):
    val=1
    for i in range(1,n+1):
        for j in range(0,i):
            print(val,end=' ')
            val +=1
        print()

def f4(n):
    val=1
    for i in range(1,n+1):
        for j in range(0,i):
            print(val,end=' ')
            val +=1
        print()
    for i in range(n,1,-1):
        for j in range(i,1,-1):
            print(val, end=' ')
            val += 1
        print()

def f6(matrix):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if row == col:
                print(matrix[row][col])

def f8(matrix):
    sum = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            sum += matrix[row][col]

    return sum

def f10(matrix):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] % 2 == 1:
                print(matrix[row][col], end=' ')
        print()

def f12(matrix1, matrix2):
    rmatrix=[]
    if len(matrix1[0]) == len(matrix2):
        for row in range(0, len(matrix1)):
            value=0
            lst = []
            for col2 in range(0, len(matrix2[0])):
                for col in range(0, len(matrix1[row])):
                    value += matrix1[row][col] * matrix2[col][col2]
                lst.append(value)
                value=0
            rmatrix.append(lst)

    return rmatrix

def f14(rows, cols):
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