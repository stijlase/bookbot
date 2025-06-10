import sys 

from stats import (
    word_count, 
    char_freq, 
    sorted_freq,
)


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


def main():
    contents = get_book_text(book_path)
    words = word_count(contents)
    freq = char_freq(contents)
    sorted_entries = sorted_freq(freq)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")
    for entry in sorted_entries:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read() 


main()