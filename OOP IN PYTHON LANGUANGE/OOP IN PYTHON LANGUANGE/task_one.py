class Person:
    def __init__(self, name, age, gender, employee_id, department):
        self.name = name
        self.age = age
        self.gender = gender
        self.employee_id = employee_id
        self.department = department

class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender, employee_id, department)
        self.assigned_tasks = set()
        
    def assign_task(self, task):
        if task not in self.assigned_tasks:
            self.assigned_tasks.add(task)
            print(f"{self.name}, you have been assigned the task: {task}.")
        else:
            print(f"{self.name}, you have already been assigned the task: {task}.")
        
    def display_employee_info(self):
        print(f"{self.name} works in {self.department}. Assigned tasks: {', '.join(self.assigned_tasks)}")

employee_1 = Employee("Arnold", 24, "male", "B24247", "Computing Department")
employee_2 = Employee("David", 28, "male", "B24256", "School of Law")

print(employee_2.name)
print(employee_2.age)
print(employee_2.gender)
print(employee_2.employee_id)
print(employee_2.department)

employee_1.assign_task("Clean your department")
employee_1.assign_task("Clean your department")  # Attempt to assign the same task again
employee_2.assign_task("Organize files")

employee_1.display_employee_info()
employee_2.display_employee_info()



class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type  # Add fuel_type here as well

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)
        self.fuel_set = set()  # Renamed to avoid method shadowing

    def add_fuel(self, fuel):
        if fuel not in self.fuel_set:
            self.fuel_set.add(fuel)
            print(f"{self.model}, you have been added fuel: {fuel}.")
        else:
            print(f"{self.model}, you have already been added some fuel: {fuel}.")

    def refuel(self):
        print(f"I am trying to refuel my {self.year} {self.model}.")

    def drive(self):
        print(f"I am driving my {self.year} {self.model}.")

    def display_vehicle_info(self):
        print(f"{self.make} {self.model} {self.year}")
        self.refuel()  # Calling the method
        print(f"Fuel types added: {', '.join(self.fuel_set)}")

car1 = Car("USA", "Tesla", 2025, "Electricity")
car2 = Car("Germany", "Mercedes-Benz", 2025, "Diesel")

car1.display_vehicle_info()
car1.drive()
