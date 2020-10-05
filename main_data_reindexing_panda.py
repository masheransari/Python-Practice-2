import pandas as pd

obj = pd.Series(["Blue","Green","Yellow"],index=[0,2,4])
print(obj)

# Now we can rearrange reindex with itself

print("-------------------------------------------")
obj1 = obj.reindex(range(5))
print(obj1)

# Now we need to place NaN to asssign Value

print("-------------------------------------------")
obj2 = obj.reindex(range(5),fill_value="Black")
print(obj2)

