def davasaan(x):
    return x // 10


# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert davasaan(0) == 0, "First"
    assert davasaan(7) == 0, "Second"
    assert davasaan(81) == 8, "Third"
    assert davasaan(199) == 19, "Fourth"
    assert davasaan(4500) == 450, "Fifth"
    assert davasaan(9999) == 999, "Sixth"
    print('Click on "Check" to get your code inspected and for real tests.')
