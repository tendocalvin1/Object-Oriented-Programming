# class Person:
#     def __init__(self,name,age,gender,employee_id,department):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.employee_id = employee_id
#         self.department = department
        
# class Employee(Person):
#     def __init__(self, name, age, gender, employee_id, department):
#         super().__init__(name, age, gender,employee_id, department)
        
#     def assign_task(self):
#         print(f"You have been assigned a task to clean your {self.department}.")
        
#     def display_employee_info(self):
#         print(f"{self.name} {self.department} {self.assign_task}")
        
    
# employee_1 =Employee("Arnold",24,"male","B24247","Computing Department")
# employee_2 =Employee("David",28,"male","B24256","School of law")

# print(employee_2.name)
# print(employee_2.age)
# print(employee_2.gender)
# print(employee_2.employee_id)
# print(employee_2.department)

# employee_1.assign_task()
# employee_2.assign_task()

# employee_1.display_employee_info()
# employee_2.display_employee_info()


# number two
class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, tank_capacity):
        super().__init__(make, model, year, fuel_type)
        self.fuel_set = set()
        self.fuel_level = 0
        self.tank_capacity = tank_capacity  # Fuel tank capacity in liters
        
    def add_fuel(self, fuel, amount):
        if self.fuel_level + amount <= self.tank_capacity:
            self.fuel_set.add(fuel)
            self.fuel_level += amount
            print(f"{self.model}, you have been added fuel: {fuel}. Current fuel level: {self.fuel_level} liters.")
        else:
            print(f"{self.model}, cannot add {amount} liters of {fuel}. Exceeds tank capacity of {self.tank_capacity} liters.")
        
    def refuel(self):
        print(f"I am trying to refuel my {self.year} {self.model}.")
        
    def drive(self):
        print(f"I am driving my {self.year} {self.model}.")
        
    def display_vehicle_info(self):
        print(f"{self.make} {self.model} {self.year}")
        self.refuel()  # Calling the method
        print(f"Fuel types added: {', '.join(self.fuel_set)}")
        print(f"Current fuel level: {self.fuel_level} liters")

car1 = Car("USA", "Tesla", 2025, "Electricity", 100)
car2 = Car("Germany", "Mercedes-Benz", 2025, "Diesel", 80)

car1.display_vehicle_info()
car1.drive()
car1.refuel()
car1.add_fuel("Electricity", 50)
car1.add_fuel("Electricity", 60)  # Attempt to add more fuel than the tank capacity

    
        


    