import datetime
def today_date ():

    return datetime.datetime.now().strftime("%S:%M:%H,%d/%m/%Y")
print(today_date())
