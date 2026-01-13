import plotly.express as px

from die import Die

# Create a two D6.
die1 = Die()
die2 = Die()

# Make some rolls and store results in a list.
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die1.num_sides + die2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
# Visualize the results.
title = "Results of rolling Two D6 1,000 Times."
labels = {'x': 'Result', "y": 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
fig.write_html('dice_visual_d2.html')