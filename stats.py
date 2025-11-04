def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents    
def text_reader(text_string):
    number_of_words = len(text_string.split())
    print(f'Found {number_of_words} total words')
    return number_of_words
    #print('Found 75767 total words')
def word_counter(text_string: str):
    print(type(text_string))
    letter_count = {}
    for letter in text_string:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in letter_count:
                #print(letter)
                letter_count[letter] = 0
            letter_count[letter] += 1
    return letter_count
def dictionary_sorter(letter_sorter: dict):
    sorted_dictionary = dict(sorted(letter_sorter.items(),key=lambda item: item[1],reverse=True))
    #print("--------- Character Count -------")
    for letter in sorted_dictionary:
        print(f"{letter}: {sorted_dictionary[letter]}")
    