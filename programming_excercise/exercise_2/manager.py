from dataclasses import dataclass
from typing import Callable, List

from models import SalesPerDay


@dataclass
class SalesPerMonth:
    def __init__(self, sales_data: dict, helper: Callable[[dict], SalesPerDay]):
        self.sales: List[SalesPerDay] = []
        self.helper = helper
        self.total_sales: float = 0
        self.load_sales(sales_data=sales_data)
        self.start_sales = self.sales[0]
        self.end_sales = self.sales[-1]
        self.is_leap_year = self.end_sales.date.month == 2 and self.end_sales.date.day == 29

    def load_sales(self, sales_data: dict) -> None:
        """

        :param sales_data:
        """
        for value in sales_data.values():
            sales_per_day = self.helper(value)
            self.total_sales += sales_per_day.value
            self.sales.append(sales_per_day)

    def show_report(self) -> None:
        """

        :return:
        """
        pad: int = 80
        columns_format: str = '| {0:30} | {1:15} | {2:25} |'

        def show_with_columns_format(date, sales, total_accumulator):
            print(columns_format.format(date, sales, total_accumulator))

        def show_header():
            show_with_columns_format('Date', 'Sales', 'Total')
            print("-" * pad)

        def show_title():
            print("=" * pad)
            print(f"Sales Report".center(pad))
            print("-" * pad)
            print('Report start date: {0:30} Starting value: {1:15}'.format(self.start_sales.date_display,
                                                                            self.start_sales.value_display))
            print('Report end date:   {0:30} Total sales:    {1:15}'.format(self.end_sales.date_display,
                                                                            str(round(self.total_sales, 4))))
            print("=" * pad)

        show_title()

        if self.is_leap_year:
            print("Leap year")
            print("=" * pad)

        show_header()

        total: float = 0
        for sales_per_day in self.sales:
            total = sales_per_day.value + total
            show_with_columns_format(
                sales_per_day.date_display, sales_per_day.value_display, round(total, 4))

        print("-" * pad)
        print(f"Total sales for the month: {self.total_sales}")
        print("=" * pad)
