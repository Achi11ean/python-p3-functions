#!/usr/bin/env python3
def my_function(param):
    print("Running my_function")
    return param + 1

print(my_function(1))
my_function_return_value = my_function(4)
print(my_function_return_value)
def greet_programmer():
    print("Hello, programmer!")
greet_programmer()
    

def greet(name):
    print(f"Hello, {name}!")
greet("Guido")

def greet_with_default(name="programmer"):
        print(f"Hello, {name}!")
greet_with_default()

num1 = 45
num2 = 55
def add(num1, num2):
    return num1 + num2
def halve(number):
    return number / 2

number = 100
