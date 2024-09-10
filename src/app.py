# Streamlit live coding script
import streamlit as st
import pandas as pd
from urllib.request import urlopen
import json
from copy import deepcopy

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

# First some MPG Data Exploration
mpg_df_raw = load_data(path="./data/mpg.csv")
mpg_df = deepcopy(mpg_df_raw)

# Add title and header
st.title("Introduction to Streamlit")
st.header("MPG Data Exploration")

#st.table(data=mpg_df)
if st.checkbox("Show Dataframe"):

    st.subheader("This is my dataset:")
    st.dataframe(data=mpg_df)

#left_column, right_column = st.columns(2)
left_column, middle_column, right_column = st.columns([3, 1, 1])

years = ["All"]+sorted(pd.unique(mpg_df['year']))
year = left_column.selectbox("Choose a Year", years)

show_means = middle_column.radio(
    label='Show Class Means', options=['Yes', 'No'])

plot_types = ["Matplotlib", "Plotly"]
plot_type = right_column.radio("Choose Plot Type", plot_types)
