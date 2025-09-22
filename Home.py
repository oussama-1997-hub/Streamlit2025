import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


st.title("Data Analysis and Visualization App")
st.write("Upload your CSV file to get started.")
st.uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if st.uploaded_file is not None:
    df = pd.read_csv(st.uploaded_file)
    st.write("Preview of the uploaded data:")
    st.dataframe(df)

df.header(10)
st.write("Data Summary:")
st.write(df.describe())
st.write("First 5 rows of the data:")
st.write(df.head())
