import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

'''print(np.mean(array))
print(np.median(array))
print(np.sum(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmax(array)) #index of maximum value'''

print(np.sum(array, axis = 0)) #sum of each column
print(np.sum(array, axis = 1)) #sum of each row