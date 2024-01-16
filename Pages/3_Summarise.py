import streamlit as st

st.title('Left Back Radar Plots')

col1, col2 = st.columns(2)
with col1:
    st.image('Plots/Dove.png', use_column_width=True)
    st.image('Plots/Fawaaz.png', use_column_width=True)
with col2:
    st.image('Plots/Ndaba.png', use_column_width=True)
    st.image('Plots/Sibande.png', use_column_width=True)

# Center the last image in a new row
col3, col4, col5 = st.columns([1,2,1])
with col4:
    st.image('Plots/Sithole.png',  use_column_width=True)