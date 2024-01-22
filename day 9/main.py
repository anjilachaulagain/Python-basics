class House:
    window = 10
    color = "red"
    door = 3
    
    def __init__(self,window,color,door):
        self.window= window
        self.color=color
        self.door=door
        # print("i was call first")
    
    def ghar(self):
        color= "green"
        print('mero ghar ko color', self.color, color)
        
    def set_color(self, color):
        self.color = color
    
# ram = House()
# ram.color ="yellow"
# print(ram.color)

binit = House(10, 'black', 5)
# binit.set_color("yellow")
print(binit.color)

# binita = House()
# binita.color = "green"
# print(binita.color)