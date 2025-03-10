username='chaiaurcode'

def fun1():
    username='codehelp'
    print(username)

print(username)
fun1()


x=99
def fun2(y):
    z=x+y
    return z

result=fun2(1)
print(result)


x=99
def f1():
    x=88
    def f2():
        print(x)
    return f2
myResult=f1()
myResult()


def original_fun(num):
    def actual_fun(x):
        return x**num
    return actual_fun

f=original_fun(2)
g=original_fun(3)
print(f)
print(g)

print(f(3))
print(g(3)) 
