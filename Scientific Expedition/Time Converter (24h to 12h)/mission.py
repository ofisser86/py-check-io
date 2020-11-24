def time_converter(time):
    # replace this for solution
    am = 'a.m.'
    pm = 'p.m.'
    hours = int(time[0] + time[1])
    minutes = time[3] + time[4]
    if hours > 12:
        return f'{hours - 12}:{minutes} {pm}'
    elif hours == 12:
        return f'12:{minutes} {pm}'
    elif time == '00:00':
        return f'{hours + 12}:{minutes} {am}'
    elif hours < 10:
        return f'{time[1]}:{minutes} {am}'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
