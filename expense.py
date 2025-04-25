# track expenses implementing the entry class
import datetime
from entries import Entry

class Expense(Entry):
    def __init__(self, date: datetime, value: float = 0, desc: str = ""):
        super().__init__(date, value, desc)
        self.type: str = "expense"

    def get_type(self) -> str:
        return self.type
    
    def toString(self) -> str:
        return f"{self.get_date():%d.%m.%Y}: {self.get_desc()} -{self.get_val():.2f}"