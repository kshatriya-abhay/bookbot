
def get_word_count(text):
    assert isinstance(text, str)
    return len(text.split())

def get_char_count(text):
    count = dict()
    assert isinstance(text, str)
    for char in text:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(dict):
    return dict["count"]

def get_sorted_letter_list(letter_dict):
    assert isinstance(letter_dict, dict)
    letter_list = []
    for key, val in letter_dict.items():
        temp = dict()
        temp["letter"] = key
        temp["count"] = val
        letter_list.append(temp)
    letter_list = sorted(letter_list, reverse=True, key=sort_on)
    return letter_list