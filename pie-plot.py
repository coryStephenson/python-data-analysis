import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show

# Data
fruits = ["apples", "banana", "grape", "strawberry", "papaya" ]
data = np.random.choice(fruits, size=100)
count_values = pd.Series(data, name="fruits").value_counts()

# Matplotlib
plt.pie(count_values.values, labels=count_values.index)
plt.show()

# Pandas
count_values.plot(kind='pie')
plt.show()

