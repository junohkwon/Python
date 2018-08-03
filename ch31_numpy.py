'''
Word file에 정리해서 제출
코드는 캡쳐해서 정리
'''


import numpy as np

#1.Create an array of size 10 filled with 0
a = np.zeros(10, float)
print(a)

#2.Set fifth value to 1 from above array
a = np.zeros(10, float)
a[4] = 1
print(a)

#3.Create an array with values ranging from 10 to 49
a = np.arange(10,50,1)
print(a)

#4.Create a 5*5 matrix with values ranging from 0 to 24
a = np.arange(0,25,1).reshape((5,5))
print(a)

#5.Create a 5*5 identity matrix
a = np.eye(5)
print(a)

#6.Create an 5*5 array with random values and find the minimum and maximum value
a = np.random.random((5,5))
print('Minimum value : ', a.min(), ' Maximum value : ', a.max())

#7.Multiply a 4*3 matrix by a 3*2 matrix
# 4*3 matrix is filled with 1
# 3*2 matrix is filled with random number

a = np.full((4,3),1)
b = np.random.randint(10, size=(3,2))
m = np.dot(a,b)
print(m)

#8.Transpose the above matrix
mt = m.transpose()
print(mt)

#9.Create two matrices ranging from 0 to 24 and 25 to 49
a = np.arange(0,25).reshape((5,5))
b = np.arange(25,50).reshape((5,5))

#Add to matrix
m_add = a+b
print(m_add)

#Substract two matrix
m_sub = a-b
print(m_sub)

