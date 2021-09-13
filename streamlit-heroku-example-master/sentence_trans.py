import streamlit as st
from sentence_transformers import SentenceTransformer
 

st.title('Hello World!')

form = st.form(key='my_form')
text_source = form.text_input(label='text_source')
text_comparaison_1 = form.text_input(label='text_comparaison_1')
text_comparaison_2 = form.text_input(label='text_comparaison_2')
text_comparaison_3 = form.text_input(label='text_comparaison_3')




submit_button = form.form_submit_button(label='Submit')



sentences = [text_source, text_comparaison_1,text_comparaison_2,text_comparaison_3]


if submit_button:
    model = SentenceTransformer('sentence-transformers/paraphrase-xlm-r-multilingual-v1')
    embeddings = model.encode(sentences)
    
    st.subheader('Data')
    st.write({"text": text_source})
    st.write({"result":embeddings})
