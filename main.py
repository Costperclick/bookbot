# import functions for stats.py

from stats import get_num_words
from stats import get_num_unique_character
from stats import get_alpha_character
from stats import sort_unique_character_count

def get_book_text(path):

    with open(path) as f:
        return f.read()

def main():

    # calling function imported :
    book_text = get_book_text("books/frankenstein.txt")
    count = get_num_words(book_text)
    char_count = get_num_unique_character(book_text)
    alpha_car = get_alpha_character(char_count)
    sorted_result = sort_unique_character_count(alpha_car)

    # putting a pretty print report :
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_result:
        print(f"{char}: {count}")
    print("============= END ===============")

main()

