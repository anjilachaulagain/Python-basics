from abc import ABC, abstractmethod


class Computer():
    def run(self,app):
        self.process(app)
        
    @abstractmethod
    def process(self,app):
        pass
    
class Mobile(Computer):
    def process(self, app):
        print(f"Mobile is running {app}")
        
class laptop(Computer):
    def process(self, app):
        print(f"Laptop is running {app}")
        
samsung = Mobile()
samsung.run("Mobile Legend")


asus = laptop()
asus.run("valorant")