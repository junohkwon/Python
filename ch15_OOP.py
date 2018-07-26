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

# class A(object):
#     pass
#
# class B(A):
#     pass
#
# a=A()
# b=B()
#
# print(type(a)==A)
# print(type(b)==A)
# print(type(a)==B)
# print(type(b)==B)
# print()
# print(isinstance(a,A))
# print(isinstance(b,A))
# print(isinstance(a,B))
# print(isinstance(b,B))

# class Person:
#     __secretCount = 0
#
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
#     def __secrectMethod(self):
#         self.__secretCount+=1
#         print(self.__secretCount)
#
# A = Person('yang li')
# A._Person__secrectMethod()  #class내부의 private Method를 접근
# print(A._Person__secretCount) #class내부의 pricate Variable을 접근

class Employee:
    empCount=0
    __secretCount=0


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d'%Employee.empCount)

    def displayEmployee(self):
        print('Name : ',self.name,', Salary : ', self.salary)

    @classmethod
    def showEmployeeCount(cls):
        return Employee.empCount


emp1 = Employee("Zara",2000)
emp2=  Employee('Manni',5000)
emp1.displayEmployee()
emp2.displayEmployee()

print(id(emp1.empCount), id(emp2.empCount), id(Employee.empCount))

print(id(emp1._Employee__secretCount), id(emp2._Employee__secretCount))


print(id(emp1.name), id(emp2.name))

print(id(emp1.displayCount), id(emp2.displayCount), id(Employee.displayCount))

print('Total Employee %d'%Employee.showEmployeeCount())

# print(Employee.__doc__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__bases__)
# print(Employee.__dict__)
