from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

FRANKENSTEIN = "books/frankenstein.txt"

# Functions
def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def main():
    book_text = get_book_text(FRANKENSTEIN)
    word_count = get_word_count(book_text)
    list_of_chars = get_sorted_list(get_char_count(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FRANKENSTEIN}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in list_of_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    
    print("============= END ===============")

# Program starts here.
main()
