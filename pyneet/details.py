import streamlit as st
import pandas as pd
from pyneet.dataframe import centerDataFrame, resultDataFrame, sampleData


center_df = centerDataFrame()
result_df = resultDataFrame()


def centerDetails():
    state_options = sorted(list(center_df['CENT_STATE'].unique()))
    st.header("Search Your Exame Center")
    col1, col2 = st.columns(2) 
    with col1:
        selected_state = st.selectbox("State Name", options=state_options)
        for state in state_options:
            if state == selected_state:
                city_options = sorted(list(center_df[center_df['CENT_STATE'] == state]['CENT_CITY'].unique()))
    with col2:
        selected_city = st.selectbox("Select Your City", options=city_options)


        
    for state in state_options:
        for city in city_options:
            if (state == selected_state) & (city == selected_city):
                result = center_df[(center_df['CENT_STATE'] == state) & (center_df['CENT_CITY'] == city)]
                result = result.rename({"CENT_CITY":"Center City", "CENT_NAME":"Center Name", "CENTNO":"Center Code"})
                if st.button("Search"):
                    st.dataframe(result[['CENT_CITY', 'CENT_NAME', 'CENTNO']], hide_index=True)









