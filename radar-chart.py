import numpy as np
import matplotlib.pyplot as plt

# Define the categories
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']

# Sample data for the radar chart
values1 = [4, 3, 2, 5, 1]
values2 = [2, 4, 3, 1, 5]

# Calculate the angle values evenly spaced around the radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Add the first angle value at the end to close the loop

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
ax.plot(angles, values1, color='skyblue', linewidth=1, linestyle='solid', marker='o', markersize=4)
ax.fill(angles, values1, color='skyblue', alpha=0.25)

# Plot the second set of values
ax.plot(angles, values2, color='lightcoral', linewidth=1, linestyle='solid', marker='o', markersize=4)
ax.fill(angles, values2, color='lightcoral', alpha=0.25)

# Set the axis limits
ax.set_ylim(0, max(max(values1), max(values2)))

# Adjust the angle positions for the category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Remove the default labels

# Add the category labels outside the radar chart
for angle, category in zip(angles[:-1], categories):
    x = np.cos(angle)
    y = np.sin(angle)
    if angle <= np.pi/2:
        ha = 'left'
        va = 'bottom'
    elif angle <= np.pi:
        ha = 'left'
        va = 'top'
    elif angle <= 3*np.pi/2:
        ha = 'right'
        va = 'top'
    else:
        ha = 'right'
        va = 'bottom'
    ax.text(x, y, category, ha=ha, va=va)

# Add a legend
ax.legend(['Values 1', 'Values 2'])

# Add a title
plt.title('Radar Chart')

# Show the radar chart
plt.show()
