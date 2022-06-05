from email.headerregistry import Group
from pandas import DataFrame, date_range
from pandas import read_csv
import datetime

import other

def init():
    _df = read_csv('students.csv')
    
    df = DataFrame(columns=_df.columns)

    df.loc[0] = [other.get_day_range(x) for x in _df.iloc[0]]
    df.loc[1] = [other.get_time_range(x) for x in _df.iloc[1]]
    df.loc[2] = _df.iloc[2].str.split(',')

    return df

def user_connected(df, nick, chanel_name):
    if not chanel_name in df:
        return
    
    f = df[chanel_name]

    if not any([x.day == datetime.date.today().day for x in f[0]]):
        return
    
    if not (f[1][0] <= datetime.datetime.now().time() <= f[1][1]):
        return

    if not nick in f[2]:
        return

    print("ok!")
