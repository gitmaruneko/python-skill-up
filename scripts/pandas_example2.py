import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

print('To Multiply all values in a series by 2')
print('--------------------------------------------------')
print(s * 2)
print('To Find the Square of all the values in a Series')
print('--------------------------------------------------')
print(s ** 2)
print('To print all the values in a series that are greater than 2')
print('--------------------------------------------------')
print(s[s > 2])
