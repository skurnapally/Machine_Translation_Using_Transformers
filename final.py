import streamlit as st
import os
import numpy as np
import time
from PIL import Image
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('./Background/Background.jpg')    
original_title = '<p style="font-family:Franklin Gothic Medium;text-align:left;color:Black; font-size: 60px;">Transformer In Action</p>'
st.markdown(original_title, unsafe_allow_html=True)
original_title = '<p style="font-family:Franklin Gothic Medium;text-align:left;color:Blue; font-size: 20px;"> by Santhosh Kurnapally</p>'
st.markdown(original_title, unsafe_allow_html=True)
note1 = '<p style="font-family:Arial;text-align:left;color:red; font-size: 20px;">Enter a sentence in English</p>'
note2 = '<p style="font-family:Arial;text-align:left;color:green; font-size: 20px;">Translation in Telugu</p>'
col1,_=st.columns(2)
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)
col1.markdown(note1,unsafe_allow_html=True)
English_Text = col1.text_input("",placeholder='Enter Text Here')
col1,_=st.columns(2)
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)
col1.markdown(note2,unsafe_allow_html=True)
if English_Text:
	with st.container():
		test = f"""<p style="font-family:Arial;text-align:left;color:Black; font-size: 20px;">{English_Text}</p>"""
		st.markdown(test,unsafe_allow_html=True)








