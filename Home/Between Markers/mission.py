def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    if begin not in text and end not in text:
        return text
    elif begin not in text:
        return text[:text.index(end)]
    elif end not in text:
        return text[text.index(begin) + len(end) - 1:]
    elif text.index(begin) > text.index(end):
        return ""
    else:
        s = text.split(begin)
        for i in s:
            if end in i:
                return i.split(end)[0]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('No [b]hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
