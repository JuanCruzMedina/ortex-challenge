import os
from typing import List, Optional
from manager import TransactionAnalyzer
from models import Transaction


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def transaction_helper(row_data: List[str or int or float]) -> Transaction:
    return Transaction(
        company_name=row_data[2],
        input_date=row_data[20],
        value_eur=float(row_data[27]),
        trade_significance=int(row_data[-4]),
        exchange=row_data[-1],
    )


if __name__ == '__main__':
    PAD: int = 50
    print('=' * PAD)
    print('Transaction Analyzer'.center(PAD))
    print('=' * PAD)
    analyzer: TransactionAnalyzer = TransactionAnalyzer(csv_file_path='2017.csv', helper=transaction_helper)

    most_used_exchange: Optional[str] = analyzer.get_most_used_exchange()
    print(f'Most used exchange: {most_used_exchange}')

    print('-' * PAD)

    company_with_highest_valueEUR: str = analyzer.get_company_with_highest_valueEUR(month=8)
    print(f'Company with highest valueEUR: {company_with_highest_valueEUR}')

    print('-' * PAD)

    transactions_per_month: dict[str, float] = analyzer.get_transactions_per_month()
    print(f'Transactions per month:')
    for transactions_month, percentage in transactions_per_month.items():
        print(f'\t- {transactions_month}: {percentage}%')
    print(f'Summary: {sum(transactions_per_month.values())}')

    print('-' * PAD)
    trade_significance_value: int = 3
    transactions_per_month: dict[str, float] = analyzer.get_transactions_per_month(
        trade_significance_value)
    print(
        f'Transactions per month by trade significance equal to {trade_significance_value}:')
    for transactions_month, percentage in transactions_per_month.items():
        print(f'\t- {transactions_month}: {percentage}%')
    print(f'Summary: {sum(transactions_per_month.values())}')

    print('=' * PAD)
