#multiple inheritance = Inherit from more than one parent class
#                       C(A,B)
# multilevel inheritance = Inherit from a parent which inherits from another parent
#                           c(B) < --B(A) <--A
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is eating.")
        
    def sleep(self):
        print(f"This {self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing.")
    

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting.")

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

class Hawk(Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.flee()
fish.hunt()

fish.hunt()
hawk.sleep()
hawk.eat()