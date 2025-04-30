from stats import get_word_count
from stats import get_char_count

# Functions
def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    char_dict = get_char_count(book_text)

    print(f"{word_count} words found in the document")
    print(char_dict)


# Program starts here.
main()
