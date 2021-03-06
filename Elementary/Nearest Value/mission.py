def nearest_value(values: set, one: int) -> int:
    # your code here
    if one in values:
        return one

    values.add(one)
    sorted_values = sorted(values)
    index_one = sorted_values.index(one)

    if index_one == 0:
        return sorted_values[1]
    elif index_one == len(sorted_values) - 1:
        return sorted_values[-2]

    nearest_1 = sorted_values[index_one - 1]
    nearest_2 = sorted_values[index_one + 1]

    if (one - nearest_1) <= (nearest_2 - one):
        return nearest_1

    return nearest_2


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
