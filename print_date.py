from datetime import date

def print_date():
    today = date.today()
    print(today)

def print_nice_date():
    today = date.today()
    print(today.ctime())

