def add_time(start, duration, day=None):
    # Split start time
    time, meridian = start.split()
    start_hr, start_min = map(int, time.split(":"))

    # Convert start_hr to 24-hour format
    if meridian == "PM" and start_hr != 12:
        start_hr += 12
    elif meridian == "AM" and start_hr == 12:
        start_hr = 0

    # Split duration
    add_hr, add_min = map(int, duration.split(":"))

    # Add minutes
    total_min = start_min + add_min
    extra_hr = total_min // 60
    final_min = total_min % 60

    # Add hours
    total_hr = start_hr + add_hr + extra_hr
    days_passed = total_hr // 24
    final_hr_24 = total_hr % 24

    # Convert back to 12-hour format
    if final_hr_24 == 0:
        final_hr = 12
        meridian = "AM"
    elif final_hr_24 < 12:
        final_hr = final_hr_24
        meridian = "AM"
    elif final_hr_24 == 12:
        final_hr = 12
        meridian = "PM"
    else:
        final_hr = final_hr_24 - 12
        meridian = "PM"

    # Weekday handling
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        day_index = weekdays.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        day_part = f", {weekdays[new_day_index]}"
    else:
        day_part = ""

    # Days note
    if days_passed == 1:
        note = " (next day)"
    elif days_passed > 1:
        note = f" ({days_passed} days later)"
    else:
        note = ""

    return f"{final_hr}:{str(final_min).zfill(2)} {meridian}{day_part}{note}"