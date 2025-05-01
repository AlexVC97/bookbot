# Functions for analyzing the text
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    num_char = {}

    for char in text:
        char = char.lower()
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    
    return num_char

def sort_on(dict):
    return dict["num"]

def get_sorted_list(num_char):
    sorted_list = []

    for char, count in num_char.items():
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = count
        sorted_list.append(new_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
