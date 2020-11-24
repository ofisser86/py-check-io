def to_camel_case(name):
    # replace this for solution
    if '_' in name:
        convert = name.split('_')
        return ''.join([i.title() for i in convert])
    return name.title()


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('my_function_name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
