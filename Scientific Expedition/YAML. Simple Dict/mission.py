def yaml(a):
    # your code here
    if len(a) > 1:
        print({k.split(':')[0]: k.split(':')[1] for k in a.split(',')})

    return 0


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex Fox,
age: 12

class: 12b"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
