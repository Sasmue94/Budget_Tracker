import csv
import os
from datetime import datetime
from entries import Entry
from expense import Expense
from income import Income

# check if savefile exists
def savefile_exists(savefile: str = "./saved_entries.csv"):
    return os.path.isfile(savefile)

# create a savefile
def create_savefile(filename: str = "saved_entries.csv", data: list[Entry] = []):
    contents = []
    for entry in data:
        contents.append([entry.get_val(), entry.get_desc(), entry.get_date(), entry.get_type()])
    with open(filename, mode="w", newline="") as savefile:
        writer = csv.writer(savefile)
        writer.writerows(contents)

# get data from savefile
def read_savefile(filename: str = "saved_entries.csv"):
    read_data = []
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
    return read_data
