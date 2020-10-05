# This is a sample Python script.
# LAB #2 Task/Practice | NU

# It's Tuple
names= ("Asher","Nabeel","Rafay")
print(names)

# It's an Array

names = ["Asher","Nabeel","Rafay",8,True,10.52,"Shehryar"]
names.append("Gaffar")
anotherList = ["Hamza","Ammar","Osama",25836.32,152]
names.extend(anotherList)
for i in range(len(names)):
    print(names[i])
print(names)