import pandas as pd

data = {
    'state': ['FL', 'FL', 'GA', 'GA','GA'],
    'year': [2010, 2011, 2008, 2010, 2011],
    'pop': [18.8, 19.1, 19.7, 9.7, 9.8]
}
frame = pd.DataFrame(data)
print(frame)

print("-------------------------------------------")
print(frame['state'])
print(frame.describe())

print("-------------------------------------------")
# Add new null Column
NaN = 'NaN'
frame['other'] = NaN
print(frame)

print("-------------------------------------------")
frame['calc'] = (frame['pop'] * 2)
print(frame)

print("-------------------------------------------")
# Now we need to get sum of all the columns respectively
print(frame[['pop','year','calc']].sum())
