#pip install langchain streamlit openai

import os
from app_secrets import OPENAI_API_KEY
import streamlit as st 
from langchain import OpenAI

#setup env variable 
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

#CREATE FRONT END 
st.title("Langchain LLM app demo")
prompt = st.text_input("Enter yout prompt here")

llm = OpenAI(model="text-curie-001", temperature=0)




if prompt:
    response = llm(prompt=prompt)
    st.write(response)