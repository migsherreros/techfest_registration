import sys

print("Welcome to SMIT TechFest!")
print("Event organized by Miguel Herreros of APPDAET BTCS2")

num_p = int (input("How many participants will register?"))
if num_p <= 0:
    print("Invalid number of participants")
    sys.exit()

participants = []
for x in range(num_p):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participants.append({"name": name, "track": track})

    print("Registered participants:")
    for participant in participants:
        print(participant["name"], participant["track"])