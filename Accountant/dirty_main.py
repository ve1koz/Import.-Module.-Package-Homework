from Accountant.application.salary import *
from Accountant.application.db.people import *
from datetime import *

print('Вариант с импортом функций из salary и people:')
calculate_salary('0')
get_employees('Вася', 'Васильев')

def get_employees(name, surname):
    print(f'{name} {surname} НЕ должен получить зарплату!\n')

def calculate_salary(salary):
    print(f'Зарплата НЕ посчитана! --> {salary} руб.')

if __name__ == '__main__':
    print('Вариант с определенными в dirty_main функциями:')
    calculate_salary('100 000')
    get_employees('Кирилл','Кириллов')
    print(datetime.now().strftime("Дата: %d/%m/%Y  Время: %H:%M:%S"))