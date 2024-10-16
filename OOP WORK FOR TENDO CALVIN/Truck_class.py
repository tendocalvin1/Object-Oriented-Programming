from car_class import Vehicle
class Truck(Vehicle):
    def __init__(self, color,has_a_trailer: bool=False):
        super().__init__(color)
        
        self.has_a_trailer = has_a_trailer

    def toString(self):
        return f"The truck is {self.color}.\nHas a trailer:{self.has_a_trailer}."
    
if __name__ == "__main__":
    truck1 = Truck("Yellow")
    print(truck1.getColor())
    print(truck1.toString())