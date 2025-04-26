import streamlit as st
import visuals as vs
import datetime
from entries import Entry
from income import Income
from expense import Expense
import save as sv

if __name__ == "__main__":

    # config
    st.set_page_config(page_title="Budget Tracker", page_icon="💲", layout="wide", initial_sidebar_state="collapsed", menu_items=None)

    entry_added: bool = False

    # create an entry
    def create_entry(type: str, val: float, desc: str, date: str) -> Entry:
        if type == "Income":
            return Income(value=val, desc=desc, date=date)
        elif type == "Expense":
            return Expense(value=val, desc=desc, date=date)

    # get correct values for summary
    def update_summary() -> None:
        income: float = 0
        expense: float = 0
        if not state.entries:
            state.income = 0
            state.expenses = 0
            state.remaining = 0
            return
        for e in state.entries:
            type_of_entry: str = e.get_type()
            current_value: float = e.get_val()
            if type_of_entry == "income":
                income += current_value
            elif type_of_entry == "expense":
                expense += current_value
            state.income = income
            state.expenses = expense
            state.remaining = income - expense

    if not sv.file_exists():
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

    update_summary()

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
            desc: str = st.text_input(label="Description", value="", key="desc")
        with ml:
            val: float = st.number_input(label="Amount:", min_value=0.00, value=0.00, key="val")
        with mr:
            date: datetime = st.date_input("Date", value="today", key="date")
        with r:
            type: str = st.selectbox(label = "Income / Expense", options=["Income", "Expense"], key="type")
        submit = st.form_submit_button("Add", use_container_width=True)
        if submit:
            new_entry: Entry = create_entry(type=state.type, val=state.val, desc=state.desc, date=state.date)
            state.entries.append(new_entry)
            state.entries.sort(key=lambda x: x.get_date(), reverse=True)
            entry_added: bool = True
            
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
                update_summary()
                st.rerun()


    if entry_added:
        sv.create_savefile(data=state.entries)
        update_summary()
        st.rerun()
    # footer area
    st.divider()