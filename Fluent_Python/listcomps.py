# Understanding list comprehensions.
symbols = '!@#$%^&'
codes = []
#for symbol in symbols:
#   codes.append(ord(symbol))

codes = [ord(symbol) for symbol in symbols]
print(codes)

# last will be accessible even after comprehension unlike symbol.
codes = [last := ord(symbol) for symbol in symbols] 
print(last)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color,size) for color in colors for size in sizes]

print(tshirts)