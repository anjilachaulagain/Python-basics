# def sum(a,b):
#     return a+b
# print(sum(1,3))


# x=lambda a, b:a+b

# # print(x(1,3))
# def myFunc(n):
#     return lambda a:a*n


# # lambda a:a*2
# my_doubler = myFunc(2)
# print(my_doubler(3))


y= lambda c, d:c+d

def myfunc(m):
    return lambda c:c*m

my_tripler = myfunc(3)
print(my_tripler(3))
