# class Grandfather:
#     house = 13
    
# class Father (Grandfather):
#     car = "lambo"
    
# class Mother:
#     jewalry = "gold"
    
# class Son(Father, Mother):
#     gaming_console = "PS5"
    
# binit = Son()
# print(binit.gaming_console)
# print(binit.car)
# print(binit.house)
# print(binit.jewalry)

class Grandfather:
    def __init__(self) -> None:
        print("I am grandfather")
        self.house = 13
        print(f'I have {self.house}')
    
class Father (Grandfather):
    def __init__(self) -> None:
        print('I am father')
        super().__init__()
        self.house = 10
        print(f'I have {self.house}')
    car = "lambo"
    
class Mother:
    def __init__(self) -> None:
        print('I am mother')
    jewalry = "gold"
    
class Son(Father, Mother):
    
    gaming_console = "PS5"
    
binit = Son(object)
print(binit.gaming_console)
print(binit.car)
print(binit.house)
print(binit.jewalry)