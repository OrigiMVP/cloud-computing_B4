import streamlit as st



import requests

st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')


API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"
headers = {"Authorization": "Bearer api_ExDDwAPxOTVmRxUIQujiZxrOUHvoofqCeJ"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()





if submit_button:
    output = query({"inputs": text})
    st.subheader('Data')
    st.write({"text": text})
    st.write({"result":output})
