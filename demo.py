from app_secrets import OPENAI_API_KEY
import os
import streamlit as st
from sql_execution import execute_sf_query
from langchain import OpenAI, LLMChain, load_prompt
from pathlib import Path
from PIL import Image

def write_to_training_file(file_path, prompt, sql):
    try:
        with open(file_path, 'w') as file:
            file.write("\n prompt : {}".format(prompt))
            file.write("\n sql : {}".format(sql))
            file.write("\n lable : 1 \n\n")
        return "success"
    except Exception as e:
        print(f"Problem in opening file: {e}")
        return "problem in opening file"

# Setup env variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Project root directory
root_path = [p for p in Path(__file__).parents if p.parts[-1] == "ai_app_demo"][0]

# Create front end
st.title("AI SQL Assistant")
user_input = st.text_input("Enter your question here")
tab_titles = ["Result", "Query", "ERD Diagram"]
tabs = st.tabs(tab_titles)

# Load the image
erd_image = Image.open(f'{root_path}/images/ERD.png')
with tabs[2]:
    st.image(erd_image)

# Create the prompt
 prompt_template = load_prompt(f"{root_path}/prompts/tpch_prompt.yaml")

llm = OpenAI(model="text-davinci-002", temperature=0.9)

sql_generation_chain = LLMChain(llm=llm, prompt=prompt_template,verbose=True)

if user_input:
    sql_query = sql_generation_chain(user_input)
    result = execute_sf_query(sql_query['text'])
    
    with tabs[0]:
        st.write(result)
    with tabs[1]:
        st.write(sql_query['text'])    