
class Garage:
    def __init__(self):
        self.vehicle = None
        
        
    def setVehicle(self,Vehicle_parked):
        self.vehicle = Vehicle_parked
        return f"The car parked is {self.setVehicle}"
        
    
    
    def toString(self):
        return f"Description of the parked vehicle {self.vehicle.toString()}"
    

    
