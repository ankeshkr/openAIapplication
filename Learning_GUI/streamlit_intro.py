import streamlit as st

#Title
st.title('my awesome streamlit app')

#header
st.header('this is a header')
st.subheader('this is a subheader')
st.text('This is some text')
st.markdown('This is some markdown')

#button
st.button('this is a button')

# checkbox
st.checkbox("this is a check box")

# radio
st.radio('radio',['option1', 'option2', 'option3'])

# select box
st.selectbox('select',['option1', 'option2', 'option3'])
st.multiselect('select',['option1', 'option2', 'option3'])

# file uploaded
st.file_uploader('File Uploaded', type = ['png', 'jpg'])

# color picker
st.color_picker('pick color')

# date input
st.date_input('enter date')

# time input 
st.time_input('enter time')

#text input
st.text_input('text input', placeholder='Enter your name...')

# number input
st.number_input('Number input', min_value=1, max_value=100, value=50)

# text area
st.text_area('text area', placeholder='enter your message here')

#slider
st.slider('slider', min_value=0, max_value=100, value= 50)

# progress bar

#import time
#my_bar = st.progress(0)
#for percentage_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percentage_complete+1)

## spinner
#with st.spinner('waiting...'):
#    time.sleep(2)


# columns
col1, col2 = st.columns(2)
with col1:
    st.header('this is col1')
    st.text('some text in col1')
with col2:
    st.header('this is col2')
    st.text('some text in col2')

# add image from file uploader and diplay it
from PIL import Image
image = st.file_uploader('upload a file', type=['png','jpg'])
if image:
    st.image(image,caption='uploaded image',use_column_width=True)