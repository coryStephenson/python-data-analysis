import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show

# Data
x = np.arange(100)
y = np.random.normal(size=100) + 5*np.sin(x/20)

# Matplotlib
plt.plot(x,y)
plt.show()

# Pandas
pd.Series(y).plot()
plt.show()

# Seaborn
sns.barplot(count_values.index,count_values.values)
plt.show()

# Bokeh
p = figure()
p.line(x=count_values.index, top=count_values.values,
width=.9)
show(p)
