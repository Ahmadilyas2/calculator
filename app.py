import streamlit as st
import math

# Functions for the calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

# Streamlit app
st.title("Scientific Calculator")

# Dropdown for operation selection
operation = st.selectbox("Select operation", 
                         ["Add", "Subtract", "Multiply", "Divide", "Power", 
                          "Square Root", "Logarithm", "Sine", "Cosine", 
                          "Tangent", "Factorial"])

# Inputs for numbers
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter the first number", step=0.01, format="%.2f")
    num2 = st.number_input("Enter the second number", step=0.01, format="%.2f")
elif operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"]:
    num1 = st.number_input("Enter the number", step=0.01, format="%.2f")

# Button to perform calculation
if st.button("Calculate"):
    if operation == "Add":
        st.write(f"Result: {add(num1, num2)}")
    elif operation == "Subtract":
        st.write(f"Result: {subtract(num1, num2)}")
    elif operation == "Multiply":
        st.write(f"Result: {multiply(num1, num2)}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {result}")
    elif operation == "Power":
        st.write(f"Result: {power(num1, num2)}")
    elif operation == "Square Root":
        st.write(f"Result: {square_root(num1)}")
    elif operation == "Logarithm":
        base = st.number_input("Enter the base (default is 10)", value=10)
        st.write(f"Result: {logarithm(num1, base)}")
    elif operation == "Sine":
        st.write(f"Result: {sine(num1)}")
    elif operation == "Cosine":
        st.write(f"Result: {cosine(num1)}")
    elif operation == "Tangent":
        st.write(f"Result: {tangent(num1)}")
    elif operation == "Factorial":
        st.write(f"Result: {factorial(int(num1))}")
