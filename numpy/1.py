import numpy as np

'''array = np.array([[['a','b','c'], ['d','e','f'], ['g','h','i']],
                  [['j','k','k'], ['m','n','o'], ['p','q','r']],
                  [['s','t','u'], ['v','w','x'], ['y','z','_']]])

print(array[1,2,0])'''

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

#print(array[::-2]) row selection
#print(array[:, : : -2]) column selection

#print(array[2::,:2:]) row-column slicing
'''print(array-1)
print(array*2)
print(array+2)
print(array/2)
print(array**2) scalar operation'''

'''print(np.round(np.sqrt(array)))
print(np.floor(np.sqrt(array)))
print(np.ceil(np.sqrt(array)))'''
#print(np.pi * array ** 2)
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

