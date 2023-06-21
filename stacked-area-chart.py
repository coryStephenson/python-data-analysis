import matplotlib.pyplot as plt

# Sample data for the stacked area chart
x = [1, 2, 3, 4, 5]  # X-axis values
y1 = [10, 20, 15, 25, 30]  # Values for the first category
y2 = [5, 15, 10, 20, 25]  # Values for the second category
y3 = [15, 5, 20, 10, 15]  # Values for the third category

# Create the stacked area chart
plt.stackplot(x, y1, y2, y3, labels=['Category 1', 'Category 2', 'Category 3'], colors=['skyblue', 'lightgreen', 'salmon'])
plt.legend(loc='upper left')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Stacked Area Chart')

# Show the stacked area chart
plt.show()
