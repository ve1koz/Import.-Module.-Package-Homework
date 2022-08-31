from Accountant.application.salary import calculate_salary
from Accountant.application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    calculate_salary('100 000')
    get_employees('Василий','Васильев')
    print(datetime.now().strftime("Дата: %d/%m/%Y  Время: %H:%M:%S"))
