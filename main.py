from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(pathname):
    with open(pathname) as f:
        book_text = f.read()
    return book_text

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    ccount = count_characters(book_text)
    sorted_list_of_dictionaries = sorted_dicts(ccount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #for each item in the list:
    #remember that the item itself is a dictionary
    for i in sorted_list_of_dictionaries:
        #get the item's char value and see if it is alphanumeric
        if i["char"].isalpha():
            print(f"{i["char"]}: {i['num']}")
    print("============= END ===============")
main()
