# basic module to show things on screen

from streamlit import success, error, container
from entries import Entry

# render empty space specified in number of pixels
def empty_space(px = 0) -> None:
    container(height=px, border=False)

# displays an entry based onits type
def display(entry: Entry) -> None:
    if entry.get_type() == "income":
        success(entry.toString())
    elif entry.get_type() == "expense":
        error(entry.toString())