import sys
from stats import *

if __name__ == "__main__":
    #print(f"{sys.argv}")
    #sys.argv.append('/Users/alyansiddiqui/bookbot/books/frankenstein.txt')
    #[1]='/Users/alyansiddiqui/bookbot/books/frankenstein.txt'
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    txt = get_book_text(f'{sys.argv[1]}')
    text_reader(txt)
    letter_counts = word_counter(txt)
    number_of_words = text_reader(txt)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    dictionary_sorter(letter_counts)
