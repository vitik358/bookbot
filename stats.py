def get_book_text (book_name):
    book_text = ""
    with open(book_name) as b:
        book_text = b.read()
    return(book_text)

def word_counter(book_text):
    book_splitted = book_text.split()
    return(len(book_splitted))

def character_counter(book_text):
    statistics = {}
    for letter in book_text:
        letter_lower_case = letter.lower()
        if letter_lower_case in statistics:
            statistics[letter_lower_case] += 1
        else:
            statistics[letter_lower_case] = 1
    return(statistics)

def dict_to_list(dictionary):
    char_list = []
    for char in dictionary:
        if char.isalpha():
            temp_dict = {}
            temp_dict["char"] = char
            temp_dict["num"] = dictionary[char]
            char_list.append(temp_dict)
    return(char_list)

def sort_on(unsorted_dict):
    return unsorted_dict["num"]

def sort_list(unsorted_dict):
 
    unsorted_dict.sort(reverse = True, key = sort_on)
    return(unsorted_dict)