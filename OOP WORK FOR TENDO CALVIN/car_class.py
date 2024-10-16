from assignment1 import Vehicle
class Car(Vehicle):
    def __init__(self,color,has_winter_tires:bool=False):
         super().__init__(color)
         
         self.has_winter_tires = has_winter_tires
         
    def toSrting(self):
        return f"The vehicle is {self.color}.\nHas winter tires:{self.has_winter_tires}."

if __name__ == "__main__":
    
    car1 = Vehicle("Violet")
    print(car1.getColor())
    print(car1.toString())
             
        
        

    
    
     
        
        