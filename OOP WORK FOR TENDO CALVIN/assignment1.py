# Car Rental
class Vehicle:
    def __init__(self,color):
        self.color = color
        
    def getColor(self):
        return f"{self.color}."
    
    def toString(self):
        return f"The vehicle has a color of {self.getColor()}."
    
Vehicle1 = Vehicle("red")
Vehicle2 = Vehicle("green")

 
if __name__ == "__main__":
    # Vehicle1 = Vehicle("red")
    # Vehicle2 = Vehicle("green")
    print(Vehicle1.getColor())
    print(Vehicle2.toString())







    
    
        
    
    
        