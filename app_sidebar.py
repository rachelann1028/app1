import streamlit as st
import pandas as pd
import numpy as np
 
st.write('# Streamlit Day 2')
st.progress(50)
st.color_picker("Pick a color", "#00f900")
st.image('images/saitlogo.jpg',None,100)

#Sidebar
st.sidebar.title("Login here")
st.sidebar.text_input("Username")
st.sidebar.text_input("Password", type="password")
st.sidebar.file_uploader("Upload a file")
st.sidebar.button("Predict")
