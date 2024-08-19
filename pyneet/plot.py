from pyneet.dataframe import centerDataFrame, resultDataFrame
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

center_df = centerDataFrame()
result_df = resultDataFrame()

def plotting():
    # 2. Total numbers of center in each state
    fig, ax= plt.subplots(figsize=(8, 6))
    ## specifiy the RGB color (red, green, blue, transparency)
    color = [0.6, 0.2, 0.8, 0.5]
    plots = center_df['CENT_STATE'].value_counts(ascending=False).head(10).plot(kind='bar', color=color, ax=ax)

    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.0f'),
                    (bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='center', size=10, xytext=(0, 8),
                    textcoords='offset points')

    plt.xlabel('State Name', size=12)
    plt.ylabel("Numbers of exam centers", size=10)
    plt.title("Total numbers of center in each state")

    st.pyplot(fig=fig)



    # 2. Total numbers of center in each state
    fig, ax = plt.subplots(figsize=(8, 6))
    ## specifiy the RGB color (red, green, blue, transparency)
    color = [0.6, 0.2, 0.8, 0.5]
    plots = center_df['CENT_CITY'].value_counts(ascending=False).head(10).plot(kind='bar', color=color, ax=ax)

    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.0f'),
                    (bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='center', size=10, xytext=(0, 8),
                    textcoords='offset points')

    plt.xlabel('State Name', size=12)
    plt.ylabel("Numbers of exam centers", size=10)
    plt.title("Total numbers of center in each state")

    st.pyplot(fig=fig)


    # 3. total numbers of center of each city
    fig, ax = plt.subplots(figsize=(8, 6))
    ## specifiy the RGB color (red, green, blue, transparency)
    color = [0.6, 0.2, 0.8, 0.5]
    plots = center_df[center_df['CENT_STATE'] == 'BIHAR']['CENT_CITY'].value_counts(ascending=False).head(10).plot(kind='bar', color=color, ax=ax)

    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.0f'),
                    (bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='center', size=10, xytext=(0, 8),
                    textcoords='offset points')

    plt.xlabel('State Name', size=12)
    plt.ylabel("Numbers of exam centers", size=10)
    plt.title("Total numbers of center of each city")

    st.pyplot(fig=fig)


    # 4. Total numbers of exam centers for Bihar states
    center_df[center_df['CENT_STATE'] == 'BIHAR']['CENT_CITY'].value_counts(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 6))
    ## specifiy the RGB color (red, green, blue, transparency)
    color = [0.6, 0.2, 0.8, 0.5]
    plots = center_df['CENT_CITY'].value_counts(ascending=False).head(10).plot(kind='bar', color=color, ax=ax)

    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.0f'),
                    (bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='center', size=10, xytext=(0, 8),
                    textcoords='offset points')

    plt.xlabel('State Name', size=12)
    plt.ylabel("Numbers of exam centers", size=10)
    plt.title("Total numbers of center of each city")

    st.pyplot(fig=fig)

def stateCentres():
    st.title("Select Your State")

    state_options = sorted(list(center_df['CENT_STATE'].unique()))
    # city_options = sorted(list(center_df['CENT_CITY'].unique()))

    selected_state = st.selectbox("State Name", options=state_options)

    if st.button("Get"):
        for state in center_df['CENT_STATE']:
            if state == selected_state:
                result = center_df[center_df['CENT_STATE'] == selected_state]
                st.dataframe(result['CENT_CITY'].value_counts().reset_index().head(10), hide_index=True)
                break

        else:
            st.warning("State is not present !")

    # # Total numbers of exam centers for Bihar states
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h4>BIHAR</4>", unsafe_allow_html=True)
        st.dataframe(center_df[center_df['CENT_STATE'] == 'BIHAR']['CENT_CITY'].value_counts(ascending=False).head(10))
    with col2:
        st.markdown("<h4>MAHARASHTRA</4>", unsafe_allow_html=True)
        st.dataframe(center_df[center_df['CENT_STATE'] == 'MAHARASHTRA']['CENT_CITY'].value_counts(ascending=False).head(10))
    with col3:
        st.markdown("<h4>UTTAR PRADESH</4>", unsafe_allow_html=True)
        st.dataframe(center_df[center_df['CENT_STATE'] == 'UTTAR PRADESH']['CENT_CITY'].value_counts(ascending=False).head(10))

    