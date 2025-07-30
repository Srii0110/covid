import streamlit as st
from PIL import Image
from prediction import fun

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image,use_column_width=True)
button=st.button("Submit")
if button:
    result = fun()
    st.success(result)
