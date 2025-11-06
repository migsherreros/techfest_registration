import sys

print("Welcome to SMIT TechFest!")
print("Event organized by Miguel Herreros of APPDAET BTCS2")

p = input("How many participants will register?")
if int(p) <= 0:
    print("Invalid number of participants")
    sys.exit()

