def add_time(start, duration, starting_day=""):
    # error handling will not be performed only on start variable
    # project reads "Assume that the start time are valid times"
    try:
        duration_hours, duration_minutes = [int(x) for x in duration.split(':')]
        if any([
            duration_hours < 0,
            duration_minutes >= 60
        ]):
            raise
    except ValueError:
        return "Error: Please check your time to add."

    weekday_mapper = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    if starting_day and starting_day.lower() not in weekday_mapper:
        return "Error: You entered an unknown weekday."

    start_hour, start_minute = start.split(':')
    start_minute, start_segment = start_minute.split()
    start_hour = int(start_hour)
    start_minute = int(start_minute)

    day_counter = 0
    start_minute = duration_minutes + start_minute
    if start_minute >= 60:
        duration_hours += 1
        start_minute -= 60

    while duration_hours > 0:
        start_hour += 1
        duration_hours -= 1

        if start_hour == 12:
            if start_segment == "PM":
                start_segment = "AM"
                day_counter += 1
            else:
                start_segment = "PM"

        if start_hour == 13:
            start_hour -= 12

    if day_counter == 1:
        day_hint = " (next day)"
    elif day_counter > 1:
        day_hint = f" ({day_counter} days later)"
    else:
        day_hint = ""

    if starting_day:
        weekday_index = weekday_mapper[starting_day.lower()]
        while day_counter > 0:
            weekday_index += 1
            day_counter -= 1
        new_weekday = f", {str([*weekday_mapper][weekday_index%7]).capitalize()}"
    else:
        new_weekday = ""

    new_time = f'{start_hour}:{start_minute:02d} {start_segment}{new_weekday}{day_hint}'

    return new_time


if __name__ == '__main__':
    print(add_time("6:30 PM", "205:12"))
