from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def bookbot(url):
    book_contents = get_book_text(url)
    word_count = count_words(book_contents)
    character_dictionary = count_characters(book_contents)
    character_list = sort_characters(character_dictionary)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for obj in character_list:
        if obj["char"].isalpha():
            print(f"{obj["char"]}: {obj["num"]}")
    print(f"============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookbot(sys.argv[1])

main()