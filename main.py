from stats import get_word_count, get_char_count, get_sorted_letter_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f"Analyzing book found at {filepath}...")
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_dict = get_char_count(text)
    letter_list = get_sorted_letter_list(letter_dict)
    for item in letter_list:
        if item["letter"].isalpha():
            print(f"{item["letter"]}: {item["count"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()