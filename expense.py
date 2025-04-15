from entries import Entry

class Expense(Entry):
    def __init__(self, date, value=0, desc=""):
        super().__init__(date, value, desc)
        self.type = "expense"

    def get_type(self) -> str:
        return self.type
    
    def toString(self) -> str:
        return f"{self.get_date()} {self.get_desc()}: -{self.get_val():.2f}"