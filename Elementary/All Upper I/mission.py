def is_all_upper(text: str) -> bool:
    # your code here
    if text.isupper():
        return True
    elif len(text) == 0 or text == " " * len(text) or text.isdigit():
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('   '))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")