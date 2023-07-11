import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("""
         Coming 2030. Our company strives to provide value and optimize solutions for our clients. We are a 
         consulting company focused on providing technical assistance. Feel free to look around and contact our 
         team for any inquiries.
""")

st.header("Current Employees")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")
df["full name"] = df["first name"] + " " + df["last name"]

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row["full name"].title())
        st.caption(row["role"])
        st.image('images/' + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["full name"].title())
        st.caption(row["role"])
        st.image('images/' + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["full name"].title())
        st.caption(row["role"])
        st.image('images/' + row["image"])