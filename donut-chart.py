import matplotlib.pyplot as plt

# Sample data for the donut chart
labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4']
sizes = [30, 20, 15, 35]
colors = ['skyblue', 'yellowgreen', 'orange', 'lightcoral']
inner_radius = 0.3  # Adjust the size of the inner hole

# Create the donut chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax.set_aspect('equal')  # Ensure a circular shape
ax.set_title('Donut Chart')

# Create a white circle in the middle to make a hole
circle = plt.Circle((0, 0), inner_radius, color='white')
ax.add_artist(circle)

# Show the donut chart
plt.show()
