import streamlit as st
st.markdown('<h1 style=font-size:40px; >Unit & Currency Converter</h1>', unsafe_allow_html=True)
centered_markdown = """
<div style="display: flex; justify-content: center; align-items: center; height: 30vh;">
    <iframe src="https://lottie.host/embed/166bec96-faad-4ed8-aa2f-8f393e6563c7/MotO6059jJ.json" width="200" height="200"></iframe>
</div>
"""
st.markdown(centered_markdown, unsafe_allow_html=True)
st.markdown('<h1>Currency</h1>', unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col1:
    curr1 = st.selectbox('Currency1',['EUR','USD','GBP','INR'])
with col2:
        st.markdown('<iframe src="https://lottie.host/embed/c36eebb5-88ec-4a33-99d2-549cee0eea4d/uikYxqE3PQ.json"></iframe>',unsafe_allow_html=True)
with col3:
    curr2 = st.selectbox('Currency 2',['EUR','USD','GBP','INR'])
if curr1=='USD':
    if curr2=='EUR': one_two=0.91
    elif curr2 == 'USD': one_two=1
    elif curr2 == 'INR': one_two=83.42
    elif curr2 == 'GBP': one_two=0.79
if curr1=='EUR':
    if curr2=='EUR': one_two=1
    elif curr2 == 'USD': one_two=1.09
    elif curr2 == 'INR': one_two=91.11
    elif curr2 == 'GBP': one_two=0.87
if curr1=='GBP':
    if curr2=='EUR': one_two=1.15
    elif curr2 == 'USD': one_two=1.26
    elif curr2 == 'INR': one_two=105.21
    elif curr2 == 'GBP': one_two=1
if curr1=='INR':
    if curr2=='EUR': one_two=0.011
    elif curr2 == 'USD': one_two=0.012
    elif curr2 == 'INR': one_two=1
    elif curr2 == 'GBP': one_two=0.0095
with col1:
    amount=st.number_input(curr1)
with col3:
    converted=amount*one_two
    st.success(converted)

st.markdown('<style> body{text-align:center;} </style>',unsafe_allow_html=True)