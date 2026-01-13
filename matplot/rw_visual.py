import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk instance.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)

    # Differentiating endpoints with green
    ax.scatter(0, 0, c='green', s=20)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=20) # Both axes will have equal spacing between tick marks.
    ax.set_aspect('equal')

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    is_running = input("Make another walk? (y/n): ")
    if is_running == 'n':
        break