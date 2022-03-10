import calendar
import csv
from collections import Counter
from dataclasses import dataclass
from typing import Callable, Optional, List

from exceptions import UnsupportedExtensionError, InvalidMonthNumberError, NoExchangesAvailableError
from models import Transaction
import os


@dataclass
class TransactionAnalyzer:
    def __init__(self, csv_file_path: str, helper: Callable[[List[str or int or float]], Transaction]):

        if csv_file_path.__eq__(""):
            raise ValueError("The file path can not be empty")

        _, file_extension = os.path.splitext(csv_file_path)

        if not file_extension.__eq__('.csv'):
            raise UnsupportedExtensionError(extension=file_extension, message='Supported files are only CSV.')

        self.csv_file_path: str = csv_file_path
        self.helper: Callable[[List[str or int or float]], Transaction] = helper
        self.transactions: List[Transaction] = []
        self.transactions_count = 0
        self.load_transactions()

    def load_transactions(self) -> None:

        with open(self.csv_file_path, 'r', encoding='UTF-8') as file:
            csvreader = csv.reader(file)
            csvreader.__next__()
            for row in csvreader:
                self.transactions.append(self.helper(row))

        self.transactions_count = self.transactions.__len__()

    def get_most_used_exchange(self) -> Optional[str]:

        exchanges = [t.exchange for t in self.transactions]

        if not exchanges:
            raise NoExchangesAvailableError(message="No exchanges available.")

        count = Counter(exchanges)
        first, second = count.most_common()[0][0], count.most_common()[1][0]

        if first.__eq__('off exchange'):
            return second

        return first

    def get_transactions_per_month(self, trade_significance: Optional[int] = None) -> dict[str, float]:

        def calculate_transactions_percentage(count: int) -> float:
            if self.transactions_count == 0:
                raise ZeroDivisionError('No transactions loaded')

            return round(count / self.transactions_count * 100, 2)

        _transactions_per_month: dict[str, int] = {}
        for transaction in self.transactions:
            if trade_significance is not None and transaction.trade_significance != trade_significance:
                continue
            _month = calendar.month_name[transaction.input_date.month]
            _transactions_count = _transactions_per_month.get(_month, 0)
            _transactions_per_month.update({_month: _transactions_count + 1})

        _percentage_per_month: dict[str, float] = {}

        for key, value in _transactions_per_month.items():
            _percentage_per_month[key] = calculate_transactions_percentage(
                count=value)

        return _percentage_per_month

    def get_company_with_highest_valueEUR(self, month: int):
        if not (1 <= month <= 12):
            raise InvalidMonthNumberError(number=month, message="Invalid month number")

        companies: dict[str, float] = {}
        for transaction in self.transactions:
            if transaction.input_date.month != month:
                continue
            combined_value = companies.get(transaction.company_name, 0)
            companies.update(
                {transaction.company_name: combined_value + transaction.value_eur})

        companies_ordered: List = sorted(companies.items(), key=lambda x: x[1])
        highest_company: str = companies_ordered[-1][0]
        return highest_company
