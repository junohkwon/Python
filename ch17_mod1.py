PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r**2)

def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print('impossible to sum')
        return
    else:
        result=sum(a,b)
    return result

if __name__ == '__main__':
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI,4.4))