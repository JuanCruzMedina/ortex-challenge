from datetime import datetime

from manager import SalesPerMonth
from models import SalesPerDay

'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
# Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}


# Do not change anything in the section above, it is just setting up some sample data

def sales_helper(data: dict) -> SalesPerDay:
    """
    Get the sales per day of a dictionary
    :param data: dictionary with sales information per day
    :return: SalesPerDay object
    """
    return SalesPerDay(date=data['date'], value=data['sales'])


if __name__ == '__main__':
    sales_per_month = SalesPerMonth(sales_data=test_data, helper=sales_helper)
    sales_per_month.show_report()
