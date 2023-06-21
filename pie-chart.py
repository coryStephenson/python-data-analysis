import matplotlib.pyplot as plt

# Sample data for the pie chart
labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4']
sizes = [30, 20, 15, 35]
colors = ['skyblue', 'yellowgreen', 'orange', 'lightcoral']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_aspect('equal')  # Ensure a circular shape
ax.set_title('Circle Chart')

# Show the pie chart
plt.show()
