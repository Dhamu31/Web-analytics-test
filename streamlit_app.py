import streamlit as st
import streamlit_analytics

with streamlit_analytics.track():
  st.text_input("Write your name:")
  st.selectbox("Select your favourite",["Kohli","Dhoni","Rohit"])
  st.button("Click me")
