class BaseClass(object):
    def printHam(self):
        print('ham')


class InhertingClass(BaseClass):
    pass


x=InhertingClass()
x.printHam()