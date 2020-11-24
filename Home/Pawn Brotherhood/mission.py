def safe_pawns(pawns) -> int:
    count = 0
    letters = 'abcdefgh'
    numbers = '12345678'
    for i in pawns:
        if i[1] == '1':
            continue
        elif i[0] == 'a':
            protect1 = None
            protect2 = letters[letters.index(i[0]) + 1] + str(numbers[numbers.index(i[1]) - 1])
        elif i[0] == 'h':
            protect1 = letters[letters.index(i[0]) - 1] + str(numbers[numbers.index(i[1]) - 1])
            protect2 = None
        else:
            protect1 = letters[letters.index(i[0]) - 1] + str(numbers[numbers.index(i[1]) - 1])
            protect2 = letters[letters.index(i[0]) + 1] + str(numbers[numbers.index(i[1]) - 1])

        if protect1 in pawns or protect2 in pawns:
            count += 1

    print(count)
    return count


if __name__ == '__main__':
    safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"])
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
