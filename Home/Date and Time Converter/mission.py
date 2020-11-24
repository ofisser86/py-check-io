def date_time(time: str) -> str:
    # replace this for solution
    time_slit = time.split('.')
    month = [0, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    holyday = 'Somebody was born'
    if int(time_slit[0]) == 1:
        holyday = 'Millenium'
    elif int(time_slit[0]) == 9:
        holyday = 'Victory'

    hour = int(time_slit[2].split()[1].split(':')[0])
    minute = int(time_slit[2].split()[1].split(':')[1])
    return f"{int(time_slit[0])} {month[int(time_slit[1])]} {time_slit[2].split()[0]} year {hour} hour{'' if hour == 1 else 's'} {minute} minute{'' if minute == 1 else 's'}"


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
