import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


st.set_page_config(layout="wide")

st.image('https://raw.githubusercontent.com/Romain056/Streamlit/main/cinecreuse.png')


main_section = st.beta_container()
plots = st.beta_container()
user_inputs = st.beta_container()

with main_section:
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Ciné Creuse</p>', unsafe_allow_html=True)
    st.text(" \n")
    st.header('**1. Statistiques sur les films:** Statistiques / Visualisation des KPIs')
    st.header('**2. Recommandations de films:** Utilisation de notre algorithme')
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")



with plots:
    st.header('1. Statistiques / Visualisation des KPIs''')

    HtmlFile = open("https://raw.githubusercontent.com/Romain056/Streamlit/main/genres_2000.html", 'r', encoding='utf-8',)
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code,height=600)

    HtmlFile = open("https://raw.githubusercontent.com/Romain056/Streamlit/main/sorties.html", 'r', encoding='utf-8', )
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=600)

    HtmlFile = open("https://raw.githubusercontent.com/Romain056/Streamlit/main/duree_2000.html", 'r', encoding='utf-8',)
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code,height=600)

    HtmlFile = open("https://raw.githubusercontent.com/Romain056/Streamlit/main/partition.html", 'r', encoding='utf-8', )
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=600)



with user_inputs:
    st.header('2. Recommandation de films')
    film = st.text_input('Veuillez choisir un film:')
