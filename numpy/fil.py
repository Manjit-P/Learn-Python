import numpy as np

ages = np.array([[21, 17, 19,20,16, 30,18,65],
                 [39,22,15,99,18,19,20,21]])

'''teen = ages[ages<18]
adult = ages[(ages>=18) & (ages<65)] 
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]'''
adults = np.where(ages >= 18, ages, 0)

print(adults)