import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly' 
# Read the CSV file
df = pd.read_csv('plots/dc_pass_da_obv.csv').iloc[:, 1:]

# Define team colors
team_colors = {
    "AmaZulu FC": "darkgreen",
    "Orlando Pirates FC": "black",
    "Cape Town Spurs": "white",
    "Sekhukhune United": "mistyrose",
    "Lamontville Golden Arrows FC": "grey",
    "Cape Town City FC": "blue",
    "Royal AM FC": "gold",
    "TS Galaxy FC": "red",
    "Kaizer Chiefs FC": "darkorange",
    "Mamelodi Sundowns FC": "yellow",
    "Stellenbosch FC": "maroon",
    "Chippa United FC": "cornflowerblue",
    "SuperSport United FC": "darkblue",
    "Swallows FC": "purple",
    "Richards Bay FC": "lightsteelblue",
    "Polokwane City": "orange"
}

# Map team colors to the dataframe
df['team_color'] = df['team_name'].map(team_colors)

# Filter for Left Backs and related positions
lbs = df[df['primary_position'].isin(['Left Back', 'Left Wing Back', 'Left Centre Back'])]

# Create scatter plot
scatter_plot = go.Figure()

scatter_plot.add_trace(
    go.Scatter(
        x=lbs['offensive'],
        y=lbs['defensive'],
        text=lbs.apply(lambda row: f"Team: {row['team_name']}<br>Age: {row['Age']}<br>Position: {row['primary_position']}", axis=1),
        mode='markers',
        marker=dict(
            color=lbs['team_color'],
            size=12,
            line=dict(color=None, width=2)
        )
    )
)

# Set layout
scatter_plot.update_layout(
    title='Offensive vs Defensive Scatter Plot',
    xaxis=dict(title='Offensive', zeroline=True),
    yaxis=dict(title='Defensive', zeroline=True),
    showlegend=False,
    hovermode='closest',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(230,230,250)',
    annotations=[
        dict(
            text=name,
            x=x,
            y=y + 0.01,
            showarrow=False,
            font=dict(size=9, color='white')
        )
        for name, x, y in zip(lbs['player_name'], lbs['offensive'], lbs['defensive'])
    ]
)

# Streamlit app
st.plotly_chart(scatter_plot)