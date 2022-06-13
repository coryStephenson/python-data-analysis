import seaborn as sns

# Data
fruits = [ <<apple>>, <<banana>>, <<grape>>, <<strawberry>>, <<papaya>> ]
stage = [ <<ripe>>, <<unripe>>, <<rotten>> ]

data_fruits = np.random.choice(fruits, size=100)
data_stage = np.random.choice(stage, size=100)
ct = pd.crosstable(data_fruits, data_stage)

# Seaborn
sns.heatmap(ct)
plt.show()
