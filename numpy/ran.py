import numpy as np

'''rng = np.random.default_rng(seed = 2)
print(rng.integers(low = 1, high = 7, size=(3,4)))'''

#print(np.random.uniform(low = -1, high=2, size=3)) uniform prob

rng = np.random.default_rng()

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)