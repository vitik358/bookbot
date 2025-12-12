from stats import get_book_text, word_counter, character_counter, dict_to_list, sort_list

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    link = sys.argv[1]
    book_text = get_book_text(link)
    word_count = word_counter(book_text)
    character_dict = character_counter(book_text)
    char_list = dict_to_list(character_dict)
    sorted_list = sort_list(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {link}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


    #print(character_dict)


main()