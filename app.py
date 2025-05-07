import streamlit as st

def calculate_square_and_cube(number):
    return number ** 2, number ** 3

st.title("Square and Cube Calculator")

number = st.number_input("Enter a number", value=0.0)
square, cube = calculate_square_and_cube(number)

st.write(f"**Square** of {number} is: `{square}`")
st.write(f"**Cube** of {number} is: `{cube}`")
