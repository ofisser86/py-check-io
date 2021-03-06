def checkio(text: str) -> str:
    text = text.lower()
    temp = {ord(letter): text.count(letter) for letter in text if letter.isalpha()}
    res = []
    maximum = max(temp, key=temp.get)

    if temp[maximum] == 1:
        maximum = chr(min(temp.keys()))
    else:
        for key, value in temp.items():
            if value == temp[maximum]:
                res.append(key)
        return chr(min(res))
    return maximum


if __name__ == '__main__':
    print("Example:")
    print(checkio("Lorem ipsum dolor sit amet"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
