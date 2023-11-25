import streamlit as st
import requests
import api

st.markdown('<iframe src="https://lottie.host/embed/db1e1472-53bf-4d21-9383-df234ff6d6da/ZdRsjnzH1u.json"></iframe>',unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col1:
    curr1 = st.selectbox('Currency1',['EUR','USD','GBP'])
with col2:
    if curr1 =='EUR':
        st.markdown('<iframe src="https://lottie.host/embed/d28e1f50-2898-4747-a02d-01439edbc13c/mfCpMXpv7t.json"></iframe>',unsafe_allow_html=True)
    elif curr1 =='USD':
        st.markdown('<iframe src="https://lottie.host/embed/d28e1f50-2898-4747-a02d-01439edbc13c/mfCpMXpv7t.json"></iframe>',unsafe_allow_html=True)
    else:
        st.markdown('<iframe src="https://lottie.host/embed/d28e1f50-2898-4747-a02d-01439edbc13c/mfCpMXpv7t.json"></iframe>',unsafe_allow_html=True)
with col3:
    curr2 = st.selectbox('Currency 2',['EUR','USD','GBP'])

