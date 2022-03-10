from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    def __init__(self, input_date: str, company_name: str, value_eur: float, trade_significance: int, exchange: str):
        self.trade_significance: int = trade_significance
        self.company_name: str = company_name
        self.exchange: str = exchange
        self.value_eur: float = value_eur
        self.input_date: datetime = self.get_date(input_date)

    @staticmethod
    def get_date(string_date: str) -> datetime:
        return datetime.strptime(string_date, '%Y%m%d')
