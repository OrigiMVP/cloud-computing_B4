import streamlit as st
from transformers import pipeline

unmasker = pipeline('fill-mask', model='bert-base-uncased')



st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    result=unmasker(text)
    st.subheader('Data')
    st.write({"text": text})
    st.write({"result":result})
