import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#rng = np.random.default_rng()
#x = rng.random(size= 4)
#y = [2, 3, 4, 5]
#plt.plot(x, y, marker='.', ms= 30, mfc= 'blue', mec = 'red', ls='dotted')
#plt.show()

df = pd.read_csv('pandas/data.csv')
#print(df)
plt.grid()
count = df['Type2'].value_counts()
plt.bar(count.index, count.values)
plt.show()