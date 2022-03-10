from dataclasses import dataclass
from datetime import datetime


@dataclass
class SalesPerDay:
    """
    Class that represents the information of sales per day
    """
    def __init__(self, date: datetime, value: float):
        self.date: datetime = date
        self.value: float = value

    @property
    def value_display(self) -> str:
        return f"{round(self.value, 4)}"

    @property
    def date_display(self) -> str:
        return f"""{self.date.strftime("%a")} {self.date.strftime("%d")}th {self.date.strftime("%B")},{self.date.strftime("%Y")}"""
