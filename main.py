import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    print(get_book_text(filepath))

from stats import count_words

#print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")

from stats import count_characters

#get_character = count_characters(get_book_text("books/frankenstein.txt"))

#print(get_character)

from stats import sort_function

final_list = sort_function(count_characters(get_book_text(sys.argv[1])))

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
print("--------- Character Count -------")
for char in final_list:
    print(f"{char['char']}: {char['num']}")
print("============= END ===============")
