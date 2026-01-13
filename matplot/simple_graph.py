import matplotlib.pyplot as plt

input = [x for x in range(6)]
squares = [x ** 2 for x in range(6)]

plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots() # subplots are used to generate multiple plots.
ax.plot(input, squares, linewidth= 3)

#Set chart title and label axes.
ax.set_title("Squared Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize= 14)
ax.set_ylabel("Square of value", fontsize= 14)

# Set size of tick labels.
ax.tick_params(labelsize= 14)

plt.show()