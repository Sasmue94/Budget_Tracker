# base class for budget tracker entries

class Entry():
    def __init__(self, date, value = 0.00, desc = ""):
        self.value = round(value, 2)
        self.desc = desc
        self.date = date

    def get_val(self) -> float:
        return round(self.value, 2)
    
    def get_desc(self) -> str:
        return self.desc
    
    def get_date(self) -> str:
        return self.date
    
    def get_type(self) -> str:
        pass
    
    def set_val(self, val = 0.00) -> None:
        if val >= 0:
            self.val = round(val, 2)
        else:
            raise ValueError("Value has to be >= 0")
        
    def set_date(self, date) -> None:
        self.date = date

    def set_desc(self, desc = "") -> None:
        self.desc = desc

    def toString(self) -> str:
        return self.toString()