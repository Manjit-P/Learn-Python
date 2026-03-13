# Understanding tuple as immutable list.

a = (10, 'alpha', [1,2])
b = (10, 'alpha', [1,2])
b[-1].append(99) 
print(a==b)
# Tuple itself is immutable but if it contains a mutable obj that 
# obj can be changed.