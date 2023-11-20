import streamlit as st
from PIL import Image

st.title("Calculator App")

def add(a,b):
    c = a + b
    return c

def sub(c,d):
    e = c - d
    return e

def mul(a,b):
    c = a * b
    return c

col1, col2 = st.columns(2)

with col1:
        x = st.number_input("Input your first number")
        y = st.number_input("Input  Your Second Number")

with col2:
     if st.button("Add"):
         st.write(add(x,y))

     if st.button("Subtract"):
         st.write(sub(x,y))

     if st.button("Multiply"):
         st.write(mul(x,y))