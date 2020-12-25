from datetime import date
from datetime import time
from datetime import datetime



def main():

    today = date.today()
    print("Todays's date is ", today)


    #Print day components

    print("Date Components ", today.day, today.month, today.year )

    print("Today's weekday # is ",today.weekday())
    days = ['mon','tue','wed','thu','fri','sat','sun']
    print("Which is a: ", days[today.weekday()])


    now = datetime.now()
    print("The current time is ", now)

    t = datetime.time(datetime.now())



if __name__ == "__main__":
    main()

