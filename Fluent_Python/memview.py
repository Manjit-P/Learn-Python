# Understanding memoryview.

from array import array

var = array('B', range(6))
m1 = memoryview(var)
# print(m1.tolist())  [0, 1, 2, 3, 4, 5]
m2 = m1.cast('b', [2,3])
# m2.tolist() [[0, 1, 2], [3, 4, 5]]
m3 = m1.cast('B', [3, 2])
# m3.tolist() # [[0, 1], [2, 3], [4, 5]]
m2[1,1] = 22
m3 [1,1] = 33

print(var) # array('b', [0, 1, 2, 33, 22, 5])
# manipulates slices of array without copying bytes.