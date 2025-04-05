from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted
import sys

#filepath = "./books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main(filepath):
    book_text = get_book_text(filepath)
    list_words = get_num_words(book_text)
    num_words = len(list_words)
    characters = get_num_chars(book_text)
    sorted_characters = get_sorted(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")

    for index in range(len(sorted_characters)):
        if (sorted_characters[index]['char']).isalpha():
            # Only print alphabetic characters
            print(f"{sorted_characters[index]['char']}: {sorted_characters[index]['count']}")
    print("============= END ===============")    

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    main(filepath)
