import numpy as np

randomList = np.random.randint(100, size=100)
# print(np.random.seed(0))

# To check how many times number is being repeating..
# using Dictionary
randomList1 = np.random.randint(100, size=100)
print(randomList1)
print("")
listDict = {}
for i in range(len(randomList1)):
    if listDict.get(randomList1[i], -1) != -1:
        count = listDict[randomList1[i]]
        count = count + 1
        listDict[randomList1[i]]=count
    else:
        count=1
        listDict[randomList1[i]]=count
print(listDict)


# Finding out like if the list contain greater than 50 values.
# First we need to check which like number is exists or not.

listCheck = randomList1>50
print(listCheck)

list = randomList1[randomList1>50]

print(list)
print((randomList1).mean())
