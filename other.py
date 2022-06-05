import csv

from pandas import DataFrame, date_range
import datetime
from dateutil.relativedelta import relativedelta

weekdays_dict = {
    "понедельник" : 0,
    "вторник" : 1,
    "среда" : 2,
    "четверг" : 3,
    "пятница" : 4,
    "суббота" : 5,
    "воскресенье" : 6
}

def parse_weekday(day_str):
    day_str = day_str.lower()
    return weekdays_dict[day_str]

def weekday_range(raw_str):
    splited = raw_str.split(' - ')
    splited = [parse_weekday(x) for x in splited]

    return splited

def get_day_range(raw_weekday_range):
    _weekday_range = weekday_range(raw_weekday_range)

    start = datetime.date.today() + relativedelta(weekday=_weekday_range[0])
    finish = start + relativedelta(weekday=_weekday_range[1])

    return date_range(start,finish, freq='1D').date

def get_time_range(raw_time_range):
    
    start, finish = raw_time_range.split(' - ')

    res = date_range(start, finish, periods=2).time
    return res

# print(get_day_range("суббота - понедельник"))
# print(get_time_range("12:00 - 22:00")[0] <= datetime.datetime.now().time() <= get_time_range("12:00 - 13:00")[1])