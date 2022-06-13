import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show

# Data
fruits = [ <<apple>>, <<banana>>, <<grape>>, <<strawberry>>, <<papaya>> ]
stage = [ <<ripe>>, <<unripe>>, <<rotten>> ]

data_fruits = np.random.choice(fruits, size=100)
data_stage = np.random.choice(stage, size=100)
ct = pd.crosstable(data_fruits, data_stage)

# Seaborn
sns.heatmap(ct)
plt.show()
