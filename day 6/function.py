# def person():
#     print('hello')
    
# print(person())

# def sum(a,b):
#     return a+b

# print(sum(1,2))

# def sum(a,b):
#     return a+b

# number = sum(1,2)
# print(number)
#

#recursion
# def number():
#     print(1)
#     number()
    
# number()

def number(n=1):
    print(n)
    if n==10:
        return
    number(n+1)
    
number()