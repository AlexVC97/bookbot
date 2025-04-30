# Functions
def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")


# Program starts here.
main()
