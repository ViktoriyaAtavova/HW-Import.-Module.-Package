from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from datetime import datetime
def now_date():
    print(datetime.now().date())

if __name__ == '__main__':
    now_date()
    cs()
    ge()
