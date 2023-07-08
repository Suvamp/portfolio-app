import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Suvam Patel")
    content = """
    Hello there. I am Suvam. This is where I keep all my python projects. Feel free to look around.
    """
    st.info(content)

content2 = """
Here are my apps. Feel free to contact me. Here is my github: https://github.com/Suvamp
"""
st.write(content2)

col3, empty_col, col4 = st.columns(1.5, 0.5, 1.5)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image('images/' + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image('images/' + row["image"])
        st.write(f"[Source Code]({row['url']})")

