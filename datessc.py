def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def generate_dates(length_of_semester, starting_day, starting_year, starting_weekday):
    calendar = [["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    start_month, start_day = starting_day.split()
    start_month = calendar[0].index(start_month)
    start_day = int(start_day) - 1

    dates = []
    current_month = start_month
    current_day = start_day
    current_year = starting_year
    day_of_week = days.index(starting_weekday)

    for _ in range(length_of_semester+1):
        date_string = f"{current_day + 1} {calendar[0][current_month]} {current_year}, {days[day_of_week]}"
        dates.append(date_string)
        
        current_day += 1
        day_of_week = (day_of_week + 1) % 7

        if is_leap_year(current_year):
            calendar[1][1] = 29
        else:
            calendar[1][1] = 28

        if current_day >= calendar[1][current_month]:
            current_day = 0
            current_month = (current_month + 1) % 12

            if current_month == 0:
                current_year += 1

    dates_l = [i for i in range(0, length_of_semester)]

    return dates, dates_l
