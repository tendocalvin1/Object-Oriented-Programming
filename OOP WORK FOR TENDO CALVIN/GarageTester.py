from Garage_class import Garage
from Truck_class import Truck


class GarageTester(Garage):
    def __init__(self):
        super().__init__()

    def getExample(self):
        # creating truck object
        truck = Truck('black', False)

        # creating an object of the garage class and putting it in the garage
        my_garage = Garage()

        # putting vehicle in the garage
        my_garage.setVehicle(truck)

        # printing the information of the vehicle that is parked in the garage
        return my_garage.toString()


if __name__ == '__main__':
    # displaying the garage tester functionality
    print(GarageTester().getExample())
    
