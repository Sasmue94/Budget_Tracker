import csv
import os
from streamlit import error
from datetime import datetime
from entries import Entry
from expense import Expense
from income import Income

# check if savefile exists
def savefile_exists(savefile: str = "./saved_entries.csv") -> None:
    try:
        return os.path.isfile(savefile)
    except Exception as e:
        error(f"An unexpected error occured \n\n {e}")

# create a savefile
def create_savefile(filename: str = "saved_entries.csv", data: list[Entry] = []) -> None:
    contents = []
    for entry in data:
        contents.append([entry.get_val(), entry.get_desc(), entry.get_date(), entry.get_type()])
    try:
        with open(filename, mode="w", newline="") as savefile:
            writer = csv.writer(savefile)
            writer.writerows(contents)
    except PermissionError as e:
        error(f"Insufficient permission, could not create savefile \n\n {e}")
    except Exception:
        error(f"An unexpected error occured \n\n {e}")

# get data from savefile
def read_savefile(filename: str = "saved_entries.csv") -> list:
    read_data = []
    try:
        with open(filename, mode="r", newline="") as savefile:
            reader = csv.reader(savefile)
            for row in reader:
                date = datetime.date(datetime.strptime(row[2], "%Y-%m-%d"))
                value = float(row[0])
                desc = row[1]
                entry_type = row[3]
                if entry_type == "income":
                    e = Income(date=date, value=value, desc=desc)
                    read_data.append(e)
                elif entry_type == "expense":
                    e = Expense(date=date, value=value, desc=desc)
                    read_data.append(e)
    except FileNotFoundError as e:
        error(f"Savefile could not be found, creating new Savefile \n\n {e}")
        create_savefile()
    except PermissionError as e:
        error(f"Insufficient permission, could not read savefile \n\n {e}")
        return []
    except Exception as e:
        error(f"An unexpected error occured \n\n {e}")

    return read_data
