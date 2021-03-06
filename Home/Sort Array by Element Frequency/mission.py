from collections import Counter


def my_print(data):
    return [str(data[0]) for _ in range(data[1])]


def frequency_sort(items):
    # your code here
    counter = Counter(items)
    ordered_counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}
    res = []
    for i in ordered_counter.items():
        res += my_print(i)

    for j in range(len(res)):
        if res[j].isdigit():
            res[j] = int(res[j])

    return res


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 4, 4, 4, 6, 6, 2, 2, 2]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
