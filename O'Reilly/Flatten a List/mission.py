def flat_list(array):
    res = []
    for i in range(len(array)):
        if type(array[i]) == list:
            res.append(*array[i])
        print('Yes')
    return 0


if __name__ == '__main__':
    assert flat_list([1, [2], 3]) == [1, 2, 3], "First"
    # assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    # assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    # assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
