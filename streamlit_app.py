import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write('Hello world!')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

add_sidebar = st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics','Individual Video Analysis'))
if add_sidebar == 'Aggregate Metrics':
    st.write("Ken Jee YouTube Aggregated Data")
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    
    count = 0

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })
    st.write(df)
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
if add_sidebar == 'Individual Video Analysis':

    df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    c = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)