from pyneet.dataframe import centerDataFrame, resultDataFrame, sampleData
import streamlit as st
import matplotlib.pyplot as plt


center_df = centerDataFrame()
result_df = resultDataFrame()

result_df['city'] = result_df['city'].apply(lambda x : x.split('/')[0])
## --------------------

def examDetails():
    pass



## 1. Total numbers of candidates
def graphAnalysis():
    total_candidate = result_df.shape[0]
    print(f"Total Candidates", total_candidate)

    # Total numbers of candidates for each city
    fig, ax = plt.subplots(figsize=(8, 8))
    ## specifiy the RGB color (red, green, blue, transparency)
    color = [0.6, 0.2, 0.8, 0.5]
    plots = result_df['city'].value_counts(ascending=False).head(10).plot(kind='bar', color=color, ax=ax)

    for bar in plots.patches:
        plt.annotate(format(bar.get_height(), '.0f'),
                    (bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='center', size=10, xytext=(0, 8),
                    textcoords='offset points')

    plt.xlabel('City Name', size=12)
    plt.ylabel("Numbers of exam centers", size=10)
    plt.title("Total numbers of candidates for each city")

    st.pyplot(fig=fig)