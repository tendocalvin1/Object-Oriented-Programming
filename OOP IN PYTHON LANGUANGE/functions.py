# basic function
def greet():
    print("Hello world!")
    
greet()

# function with parameters.
def add(a,b):
    return a+b

result = add(3,5)
print(result)


def division(c,d):
    return c/d
result = division(10,5)
print(result) 

# functions with default arguments.
def greet(name = "Guest"):
    print(f"Hello {name}!")
    
greet("Arnold")
greet()


# Function with Variable Length Arguments
def add_all(*args):
    return sum(args)

result = add_all(2,4,6,8,10)
print(result) # output: 30.


# Function with Keyword Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Rex")
describe_pet(pet_name="Whiskers", animal_type="cat")

# This describe_pet function takes keyword arguments, allowing the order to be flexible when calling the function.







