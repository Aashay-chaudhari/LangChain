import streamlit as st
from langchain_helper_rest_name import generate_name_and_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican"))

if st.button('Create'):
    response = generate_name_and_items(cuisine)
    st.header(response['rest_name'])
    menu_items = response['menu_items'][2:].split("$")
    st.header("MENU ITEMS")
    for items in menu_items:
        st.write(items)
    promos = response['promos'].split(",")
    st.header("PROMOS")
    for promo in promos:
        st.write(promo)
