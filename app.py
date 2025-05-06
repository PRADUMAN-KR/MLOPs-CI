import streamlit as st

# Title
st.title("Square and Cube Calculator")

# User input
number = st.number_input("Enter a number", value=0.0)

# Calculations
square = number ** 2
cube = number ** 3

# Display results
st.write(f"**Square** of {number} is: `{square}`")
st.write(f"**Cube** of {number} is: `{cube}`")
