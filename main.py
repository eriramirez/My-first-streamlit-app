# To run this app you have to use the following command in Shell
# streamlit run main.py --server.enableCORS false --server.enableXsrfProtection=false

import streamlit as st

st.write("helloworld")

operation = st.selectbox("Operation", ["+", "-"])

a = st.text_input("A", value=0)
a = float(a)

b = st.text_input("B", value=0)
b = float(b)

if operation == "+":
  c = a + b
if operation == "-":
  c = a - b

st.write(c)
