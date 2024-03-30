import datetime


def getTime(string):
    vals = string.split(" ")
    n = int(vals[0]) # numeric value
    u = vals[1] # unit
    time = datetime.datetime.now(tz=datetime.timezone.utc)
    if u.startswith("min"):
        newTime = minusMinute(n, time)
    elif u.startswith("hour"):
        newTime = minusHour(n, time)
    elif u.startswith("day"):
        newTime = minusDay(n, time)
    elif u.startswith("week"):
        newTime = minusDay(n*7, time)
    elif u.startswith("mon"):
        newTime = minusMonth(n, time)
    else:
        print("current time")
        newTime = datetime.datetime.now()
    print(newTime)
    return newTime

def minusYear(years:int, time:datetime.datetime):
    if(years >= time.year):
        print("year can't be negative or zero")
        return time
    else:
        time = time.replace(year=time.year-years)

def minusMonth(months, time:datetime.datetime):
    dif = (-1)*months
    if(months >= time.month):
        minusYear(1, time)
        dif = 12 - months
    time = time.replace(month=time.month+dif)
    return time

def minusDay(day, time:datetime.datetime):
    dif = (-1)*day
    if(day >= time.day):
        minusMonth(1, time)
        dif = 30 - day
    time = time.replace(day=time.day+dif)
    return time

def minusHour(hour, time:datetime.datetime):
    dif = (-1)*hour
    if(hour > time.hour):
        minusDay(1, time)
        dif = 24 - hour
    time = time.replace(hour=time.hour+dif)
    return time

def minusMinute(minutes, time:datetime.datetime):
    dif = (-1)*minutes
    if(minutes > time.minute):
        minusHour(1, time)
        dif = 60 - minutes
    time = time.replace(minute=time.minute+dif)
    return time


if __name__=="__main__":
    print(getTime("2 minutes ago"))