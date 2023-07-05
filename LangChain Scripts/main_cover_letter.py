import streamlit as st
from langchain_helper_cover_letter import generate_cover_letter
import json


st.title("Create Cover Letter")
user_input = st.text_area("Enter the requirements of Job Description. ")


if st.button('Create Cover Letter'):
    response = generate_cover_letter(user_input)
    json_object = json.loads(response)
    st.write(json_object)
    company_name = json_object['company_name']
    cover_letter = json_object['cover_letter']
    f = open(company_name + '.txt', "x")
    f = open(company_name + '.txt', "w")
    f.write(cover_letter)
    f.close()