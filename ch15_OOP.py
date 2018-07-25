# class BaseClass(object):
#     def printHam(self):
#         print('ham')
#
#
# class InhertingClass(BaseClass):
#     pass
#
#
# x=InhertingClass()
# x.printHam()

# class Person:
#     #생성자를 override해서 구현함
#     def __init__(self,name):
#         self.name = name
#
#     def sayHello(self):
#         print('Hello, my name is ', self.name)
#
#     def PrintName(self):
#         print(self.name)
#
#     #소멸자를 override해서 구현함
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print('%s says bye'%self.name)
#         print(class_name,' destroyed')
#
# import sys
#
# A = Person('yang li')
# # A.sayHello()
# # A.PrintName()
# # print(A.name)
# # del A
#
# print('A refCount: ',sys.getrefcount(A))
# b=A
# print('A refCount: ',sys.getrefcount(A))
# c=A
# print('A refCount: ',sys.getrefcount(A))
# print('A address: ',id(A),' b address: ', id(b),' c adress: ', id(c))
#
# print('del A')
# del A # reference가 존재하므로 garbage collector 실행안함
# print('del B')
# del b # reference가 존재하므로 garbage collector 실행안함
# print('del C')
# del c # garbage collector 실행


# class Parent:
#     def myMethod(self):
#         print('Calling parent method')
#
# class Child(Parent):
#     def myMethod(self):
#         print('Calling child method')
#
# c = Child()
# c.myMethod()

class A(object):
    pass

class B(A):
    pass

a=A()
b=B()

print(type(a)==A)
print(type(b)==A)
print(type(a)==B)
print(type(b)==B)
print()
print(isinstance(a,A))
print(isinstance(b,A))
print(isinstance(a,B))
print(isinstance(b,B))
