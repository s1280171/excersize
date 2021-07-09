import random

print("Rolling the dice...")
num1=random.randint(1,6)
num2=random.randint(1,6)
num3=num1+num2
print("Die 1: ",num1)
print("Die 2: ",num2)
print("Total value:",num3)

if num3>7:
    print("You won")

else:
    print("You lost")