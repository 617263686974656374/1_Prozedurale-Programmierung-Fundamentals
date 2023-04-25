from datetime import date, timedelta

try:
    start_date = input("start date: ")
    end_date = input("end date: ")
    holiday = int(input("How many holidays do you have ?: "))
    start_day, start_month, start_year = [int(x) for x in start_date.split(".")]
    end_day, end_month, end_year = [int(x) for x in end_date.split(("."))]
    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    total_days = 0
    start_day_up = start_date
    while start_day_up <= end_date:
        if start_day_up.weekday() < 5:
            total_days += 1
        start_day_up += timedelta(days=1)

    if total_days > holiday:
        newend = start_date + timedelta(days=holiday )
        while newend.weekday() >= 5:
           newend += timedelta(days=1)
        print("You tried take", total_days, "days for holiday, but you have only", holiday, "days at the moment. You can take holiday until: ",
              newend.strftime('%d.%m.%Y'))
        print("You need ", holiday - total_days, " days more holidays")
    else:
        print("You will take:", total_days, "days holiday")
        print("After your holiday your free holiday are: ", holiday - total_days, "days")

except ValueError:
    print("Write correct format please ! For example: date(23.01.2023), holidays : 5")