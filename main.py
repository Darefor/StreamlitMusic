import streamlit as st
from usedb import usedb
from use_content import content
from use_section import section

engine = usedb()

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.title(":blue[Квітка Цісик]")
    st.image("images/Kacey — голос Ford’а.png")
    st.header(":blue[Душа українського народу]")

with col2:
    st.subheader(":blue[Зміст]")
    params = [col1, col2]
    sel = content(engine, params)
    section(engine, sel, params)






