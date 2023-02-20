import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Create sample data with four columns


# Create a list of column names for the histogram
# Set up the sidebar to allow the user to select a column
# Set up the sidebar to allow the user to select a column
# Set up the sidebar to allow the user to select a column
selected_dataset = st.sidebar.selectbox("Select a column", ["Karate","Polbooks","Dolphin","Football","Synthétique"])
if selected_dataset not in ["Polbooks", "Synthétique"]:
    selected_chart = st.sidebar.selectbox("Select a chart", ["article","notre"])
else:
    selected_chart = st.sidebar.selectbox("Select a chart", ["notre"])

if selected_dataset == "Synthétique":
    selected_mu = st.sidebar.selectbox("Select a value for mu", ["0.1","0.2","0.3","0.6","0.9"])

if selected_chart == "article":
    data = pd.DataFrame({
    "Karate" : ["0.42","-", "0.37","0.36","0.31","0.34"], 
    "Football"  : ["-", "-","0.588","0.58","0.57","0.58"],
    "Dolphin"    : ["0.51", "0.48","0.5","0.48","0.42","0.58"],
      "Polbooks" : ["-","-","-","-","-","-"]

}, index = ["louvain","clique-louvain","LPA","LPA-prec","LPA-max","LPA-prec-max"])
elif selected_dataset != "Synthétique":
    data  = pd.DataFrame({
    "Karate" : ["0.4","0.43","0.3821"," 0.3515","0.3600","0.3515"], 
    "Football"  : ["0.56", "0.60","0.5807","0.5698","0.5831","0.5698"],
    "Dolphin"    : ["0.46", "0.51"," 0.4917","0.4303","0.4492","0.4303"],
    "Polbooks" : ["0.52","0.53","0.4718","0.5049","0.3851","0.5049"]

}, index = ["louvain","clique-louvain","LPA","LPA-prec","LPA-max","LPA-prec-max"])
else:
    data  = pd.DataFrame({
    "0.1" : ["0.65","0.65","0.6","0.65","0.65","0.65"], 
    "0.2"  : ["0.55","0.55","0.55","0.44","0.35","0.44"],
    "0.3"    : ["0.45","0.45","0.35","0.26","0.43","0.21"],
    "0.6" : ["0","0.15","0.001","0.02","0.015","0.02"],
    "0.9" : ["0","0","0","0","0","0"]

}, index = ["louvain","clique-louvain","LPA","LPA-prec","LPA-max","LPA-prec-max"])
   
columns = list(data.columns)
st.write(data)

# Create a DataFrame with the selected column as the index and the values of a cell
if selected_dataset == "Synthétique":
    values_df = pd.DataFrame(data[selected_mu].values, index=data.index, columns=["Value"])
else:
    values_df = pd.DataFrame(data[selected_dataset].values, index=data.index, columns=["Value"])

# Create a bar chart with the flipped axes
fig = px.bar(values_df, x=values_df.index, y="Value")

# Add labels to the chart
fig.update_layout(
    xaxis_title="Index",
    yaxis_title=selected_dataset,
    title=f"Distribution of {selected_dataset}"
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)