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