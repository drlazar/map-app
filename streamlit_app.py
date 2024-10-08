import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.write("""
# Map Coordinates Application
"""
)

st.header("Please enter your desired coordinates below")

col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input("Latitude:", value = 39.32889, format="%.5f")
with col2:  
    longitude = st.number_input("Longitude:", value = -76.62028, format="%.5f")

coord = pd.DataFrame({
                        "latitude" : [latitude], 
                        "longitude" : [longitude]
                    }
                    )

st.map(coord, latitude="latitude", longitude="longitude", zoom = 13)