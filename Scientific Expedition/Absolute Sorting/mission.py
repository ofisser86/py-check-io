def checkio(numbers_array: tuple) -> list:
    less_zero = []
    for i in numbers_array:
        if i < 0:
            less_zero.append(abs(i))

    new_array = sorted([abs(i) for i in numbers_array])
    for i in range(len(new_array)):
        if new_array[i] in less_zero:
            new_array[i] *= -1

    return new_array


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))


    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)


    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
