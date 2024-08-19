import pandas as pd
import numpy as np
import streamlit as st

center = 'csv_file/centers.csv'
result = "csv_file/NEET_2024_RESULTS.csv"

def centerDataFrame(file_path=center):
    df = pd.read_csv(file_path)
    return df


def resultDataFrame(file_path=result):
    df = pd.read_csv(file_path)
    return df


center_df = centerDataFrame()
result_df = resultDataFrame()


def sampleData():
    center_df = centerDataFrame()
    result_df = resultDataFrame()

    center_df['CENT_STATE'] = center_df['CENT_STATE'].apply(lambda x: x.split()[0])
    center_df['CENT_CITY'] = center_df['CENT_CITY'].apply(lambda x: x.split()[0])

    result_df['state'] = result_df['state'].apply(lambda x: x.split()[0])

    st.header("Result Data")
    st.dataframe(result_df.head(), hide_index=True)
    st.header("Center Data")
    st.dataframe(center_df.head(), hide_index=True)

def dataAnalysis():
    # 1. Total Numbers of exam centers
    total_exam_centers = center_df['CENT_NAME'].value_counts().sum()
    st.markdown(f"<h3>Total Exam centers {total_exam_centers}</h3>",\
                unsafe_allow_html=True)
    # Total numbers of center in each state
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h4>Total centers in each State</h4>", unsafe_allow_html=True)
        st.dataframe(center_df['CENT_STATE'].value_counts(ascending=False).head(10).reset_index(), hide_index=True)
    with col2:
        st.markdown("<h4>Total centers in each City<h4>", unsafe_allow_html=True)
        st.dataframe(center_df['CENT_CITY'].value_counts(ascending=False).head(10).reset_index(), hide_index=True)

    

