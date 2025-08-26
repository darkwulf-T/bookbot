def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    print(get_book_text(filepath))

#from stats import count_words

#print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")

from stats import count_characters

get_character = count_characters(get_book_text("books/frankenstein.txt"))

print(get_character)