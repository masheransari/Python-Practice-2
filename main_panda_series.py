import pandas as pd
import numpy as np

# We can assume that we have a data sample in form of series list.

# In Series the panda would generate a series of sequence index in every row by default.
# We can simple pass array or list in series constructor like that

print("-------------------------------------------")
list1 = [1, 2, 3, 4, 5, 6, "Asher", "Nabeel", "A. Rafay", "Shehryar", 7, 8, 9, 10]
s1 = pd.Series(list1)
# print(s1)

print("-------------------------------------------")
# Or we can provide list like that as well.
s2 = pd.Series(list('123abcdefgh'))
print(s2)

# Althrough we can provide a custom index as well. like
print("-------------------------------------------")
listValues = [1, 2, 3, 4, 5, 6, "Asher", "Nabeel", "A. Rafay", "Shehryar", 7, 8, 9, 10]
listIndex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# Now this two arrays need to pass in Series Constructor
s3 = pd.Series(listValues, index=listIndex)
print(s3)

# Print Specific index which you are looking for.
print(s3['g'])

# Print multiple index in one print statement
print(s3[['g', 'h', 'i', 'j', 'k']])
print("-------------------------------------------")


dictionary1 = {'b': 100, 'c': 200, 'd': 300, 'e': 400}
s4=pd.Series(dictionary1)
print(s4)

print("-------------------------------------------")
# Now we need to add "a" index which is not define.
s5 = pd.Series(dictionary1,index=list("abcde"))
print(s5)