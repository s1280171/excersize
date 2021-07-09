import random

name=input("What is your name?")
print("Hello, ",name,"!")

print("Rolling the dice...")
num1=random.randint(1,6)
num2=random.randint(1,6)
print("Die 1: ",num1)
print("Die 2: ",num2)
print("Total value:",num1+num2)
