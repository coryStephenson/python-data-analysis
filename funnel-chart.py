import plotly.graph_objects as go

# Sample data for the funnel chart
labels = ['Step 1', 'Step 2', 'Step 3', 'Step 4']
values = [100, 70, 50, 30]

# Create the funnel chart
fig = go.Figure(go.Funnel(
    y=labels,
    x=values,
    textposition='inside',
    textinfo='value+percent initial'
))

fig.update_layout(title='Funnel Chart')

# Show the funnel chart
fig.show()
