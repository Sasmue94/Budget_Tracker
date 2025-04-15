import streamlit as st
from entries import Entry

def empty_space(px = 0):
    return st.container(height=px, border=False)

def display(entry: Entry) -> None:
    if entry.get_type() == "income":
        st.success(entry.toString())
    elif entry.get_type() == "expense":
        st.error(entry.toString())