# basic module to show things on screen

import streamlit as st
from entries import Entry

# render empty space specified in number of pixels
def empty_space(px = 0):
    return st.container(height=px, border=False)

# displays an entry based onits type
def display(entry: Entry) -> None:
    if entry.get_type() == "income":
        st.success(entry.toString())
    elif entry.get_type() == "expense":
        st.error(entry.toString())