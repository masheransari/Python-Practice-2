import numpy as np

array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8,9,10])

# (1*6) + (2*7) + (3*8) + (4*9) + (5*10) = 130
print(array1@array2)
