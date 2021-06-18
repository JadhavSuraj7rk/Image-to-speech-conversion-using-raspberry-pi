import datetime


def date_time():
    now = datetime.datetime.now()

    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
