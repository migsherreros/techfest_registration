import sys

print("Welcome to SMIT TechFest!")
print("Event organized by Miguel Herreros of APPDAET BTCS2")

num_p = int (input("\nHow many participants will register?"))
if num_p <= 0:
    print("Invalid number of participants")
    sys.exit()

participants = []
for x in range(num_p):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participants.append({"name": name, "track": track})

print("\nRegistered participants:")
count = 1
for participant in participants:
    print(count,"." ,participant["name"], "-", participant["track"])
    count += 1

unique_tracks = set()
for participant in participants:
    unique_tracks.add(participant["track"])

print("\nTracks offered in this event:")
if len(unique_tracks) < 2:
    print("Not enough variety in tracks.")
else:
    print(",".join(unique_tracks))

names_seen = set()
duplicates = set()

for participant in participants:
    name = participant["name"]
    if name in names_seen:
        duplicates.add(name)
    else:
        names_seen.add(name)
if len(duplicates) > 0:
    for name in duplicates:
        print("\nDuplicate name found:", name)
else:
    print("\nNo duplicate names.")

track_summary = {}

for participant in participants:
    track = participant["track"]
    if track in track_summary:
        track_summary[track] += 1
    else:
        track_summary[track] = 1

print("\nParticipants per track:")
for track in track_summary:
    print(track, ":", track_summary[track])