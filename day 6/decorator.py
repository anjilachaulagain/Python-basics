# def Star(func):
#     def wrapper():
#         print('*'*10)
#         func()
#         print('*'*10)
#     return wrapper
# def Hash(func):
#     def wrapper():
#         print('#'*10)
#         func()
#         print('#'*10)
#     return wrapper
# @Hash
# @Star
# def hello():
#     print('hello')
    
# def bye():
#     print('bye')
    
# hello()

def Hash(func):
    def wrapper():
        print('#'*10)
        print('*'*10)
        func()
        print('*'*10)
        print('#'*10)
    return wrapper

def hello():
    print('hello')
    
def bye():
    print('Bye')

Hash(bye)()

         