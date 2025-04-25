import streamlit as st
import visuals as vs
from entries import Entry
from income import Income
from expense import Expense
import save as sv

# config
st.set_page_config(page_title="Budget Tracker", page_icon="💲", layout="wide", initial_sidebar_state="collapsed", menu_items=None)

entry_added = False

def create_entry(type: str, val: float, desc: str, date: str) -> Entry:
    if type == "Income":
        return Income(value=val, desc=desc, date=date)
    elif type == "Expense":
        return Expense(value=val, desc=desc, date=date)


if not sv.savefile_exists():
    sv.create_savefile()

# session state
state = st.session_state

if "entries" not in state:
    state.entries = sv.read_savefile()
if "income" not in state:
    state.income = 0.00
if "expenses" not in state:
    state.expenses = 0.00
if "remaining" not in state:
    state.remaining = round(state.income - state.expenses, 2)

# header area
st.header("Budget Tracker")
st.divider()

# get correct values for summary
income = 0
expense = 0
for e in state.entries:
    type_of_entry = e.get_type()
    current_value = e.get_val()
    if type_of_entry == "income":
        income += current_value
    elif type_of_entry == "expense":
        expense += current_value
    state.income = income
    state.expenses = expense
    state.remaining = income - expense

# summary area
inc, exp, rem = st.columns(3)
with inc:
    st.subheader("Sum Income: ")
    st.subheader(f"{state.income:.2f}€")
with exp:
    st.subheader("Sum Expenses: ")
    st.subheader(f"{state.expenses:.2f}€")
with rem:
    st.subheader("Remaining: ")
    st.subheader(f"{state.remaining:.2f}€")

st.divider()

# input form area

with st.form("entry_form", border=False):
    st.subheader("Add a new entry")
    l, ml, mr, r = st.columns(4)
    with l:
        desc = st.text_input(label="Description", value="", key="desc")
    with ml:
        val = st.number_input(label="Amount:", min_value=0.00, value=0.00, key="val")
    with mr:
        date = st.date_input("Date", value="today", key="date")
    with r:
        type = st.selectbox(label = "Income / Expense", options=["Income", "Expense"], key="type")
    submit = st.form_submit_button("Add", use_container_width=True)
    if submit:
        new_entry = create_entry(type=state.type, val=state.val, desc=state.desc, date=state.date)
        state.entries.append(new_entry)
        state.entries.sort(key=lambda x: x.get_date(), reverse=True)
        entry_added = True
        
st.divider()

# display area
for i, e in enumerate(state.entries):
    l, r = st.columns([3,1])
    with l:
        vs.display(e)
    with r:
        if st.button("delete", key=f"entry_{i}", use_container_width=True):
            state.entries.pop(i)
            sv.create_savefile(data=state.entries)
            st.rerun()


if entry_added:
    sv.create_savefile(data=state.entries)
    st.rerun()

# footer area
st.divider()