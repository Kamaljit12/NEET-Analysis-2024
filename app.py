import streamlit as st
import pandas as pd
from pyneet.dataframe import centerDataFrame, resultDataFrame, sampleData
from pyneet.details import centerDetails, searchCenter, stateSearch
from pyneet.plot import stateCentres
from pyneet.dataframe import dataAnalysis
from pyneet.plot import plotting
import matplotlib.pyplot as plt
# import seaborn as sns

# app favicon logo

from PIL import Image

favicon = Image.open("img/NEET-logo.png")
# Set the page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=favicon,
    layout="wide"
)

col1, col2, col3, col4, col5  = st.columns(5)

with col1:
    st.title("Find Exam Center")
with col5:
    st.image('img/neet-ug.jpg', width=150)

center_df = centerDataFrame()
result_df = resultDataFrame()



## side bar options
options = ['Exam Centers', 'Exam Analysis', "Center Analysis",'Datasets']
selected_option = st.sidebar.selectbox("Menu", options=options)

if selected_option == 'Exam Centers':

    ## fine exam centers using state and city

    centerDetails()

    searchCenter()
    # ========================================================================
    stateSearch()

elif selected_option == 'States':
    stateCentres()

elif selected_option == 'Center Analysis':
    plotting()
    stateCentres()
    dataAnalysis()
else:
    sampleData()