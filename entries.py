# base class for budget tracker entries

import datetime

class Entry():
    def __init__(self, date: datetime, value: float = 0.00, desc: str = ""):
        self.value: float = round(value, 2)
        self.desc: str = desc
        self.date: datetime = date

    def get_val(self) -> float:
        return round(self.value, 2)
    
    def get_desc(self) -> str:
        return self.desc
    
    def get_date(self) -> str:
        return self.date
    
    def get_type(self) -> str:
        pass
    
    def set_val(self, val: float = 0.00) -> None:
        if val >= 0:
            self.val = round(val, 2)
        else:
            raise ValueError("Value has to be >= 0")
        
    def set_date(self, date: datetime) -> None:
        self.date = date

    def set_desc(self, desc: str = "") -> None:
        self.desc = desc

    def toString(self) -> str:
        return self.toString()