# track income implementing the entry class
from entries import Entry
import streamlit as st

class Income(Entry):
    def __init__(self, date, value=0, desc=""):
        super().__init__(date, value, desc)
        self.type = "income"
    
    def get_type(self) -> str:
        return self.type

    def toString(self) -> str:
        return f"{self.get_date():%d.%m.%Y}: {self.get_desc()} {self.get_val():.2f}"