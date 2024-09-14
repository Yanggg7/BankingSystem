import calendar
from datetime import datetime

def is_first_day_of_month(date):
    """check if the date is the first day of the month"""
    return date.day == 1

def is_last_day_of_month(date):
    """check if the date is the last day of the month"""
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.day == last_day