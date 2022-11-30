import streamlit as st
st.title("Addition of two numbers")

a=st.number_input("Enter First Number:")
b=st.number_input("Enter Second Number:")
c= a + b


st.write("Addition of two number is = ", c)
