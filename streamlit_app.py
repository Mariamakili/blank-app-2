import streamlit as st

st.title("🎈 exercise.py")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Load the dataset
@st.cache_data()
def load_data():
    df = pd.read_csv('unicorns.csv')
    return df

# Pre-process the data
def pre_process(df):
    df['Date Joined'] = pd.to_datetime(df['Date Joined'])
    return df

st.title('Unicorns')

df = load_data()
df = pre_process(df)

st.header('Companies by Country')

fig, ax = plt.subplots(figsize=(6.4, 2.4))

# Count the number of companies by country
# TODO

# Plot the number of companies by country
# TODO

ax.set_title('Number of Companies by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Companies')

st.pyplot(fig)

