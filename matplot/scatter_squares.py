import matplotlib.pyplot as plt

x_values = [x for x in range(1, 1001)]
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn-v0_8-deep")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# Set chart title and label axis.
ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='sci')

# plt.show()
plt.savefig('squares_plot.png', bbox_inches= 'tight') # Saves plot as external file.