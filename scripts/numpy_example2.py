import numpy as np

A = np.array([2,3,4,50])
R = np.array([8,9,10,11,15])
C = np.concatenate((A,R))

print(C)  # Output: 5
