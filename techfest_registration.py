import sys

print("Welcome to SMIT TechFest!")
print("Event organized by Miguel Herreros of APPDAET BTCS2")

num_p = int (input("How many participants will register?"))
if num_p <= 0:
    print("Invalid number of participants")
    sys.exit()