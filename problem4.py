"""4) Objective: You are given a Python class with a method that needs to be updated dynamically (i.e., monkey patched) 
to alter its behavior. Write a Python program that demonstrates 
how to use monkey patching to change the method of a class at runtime.

Problem Statement:
You have a Car class with a method start_engine() that prints a simple message: "Engine started!". Your task is to:

Dynamically modify the start_engine() method to print "Engine started with a roar!" instead of the original message.
Use monkey patching to change the behavior of start_engine() at runtime.

Class Definition:
python:- 

class Car:
    def start_engine(self):
        print("Engine started!")

Expected Output:

# Before patching
car = Car()
car.start_engine()
# Output: Engine started!

# After patching
car.start_engine()
# Output: Engine started with a roar
# """
class Car:
    def start_engine(self):
        print("engine started")
car=Car()
print("Before Patching:")
car.start_engine()
def new_start_engine():
    print("Engine started with a roar!")

car.start_engine=new_start_engine
print("After Patching:")
car.start_engine()