def sun_angle(time):
    # replace this for solution
    h, m = time.split(':')
    minutes = int(h) * 60 + int(m)
    if 1080 < minutes or minutes < 360:
        return "I don't see the sun!"

    return (minutes - 360) * 0.125 * 2


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
