def main():
    # reads the book
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book_content = f.read()

    # counts the words
    word_count = len(book_content.split())

    # counts the letters
    dict_list = []
    letter_dict = {}
    for letters in book_content:
        lower_words = letters.lower()
        if lower_words in letter_dict:
            letter_dict[lower_words] += 1
        else:
            letter_dict[lower_words] = 1

    # create dict for each letter
    for char in letter_dict:
        count = letter_dict[char]
        new_dict = {'char': char, 'count': count}
        if char.isalpha():
            dict_list.append(new_dict)

    # returns
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in this book.")
    for item in dict_list:
        print(f"The letter {item['char']} was found {item['count']} times.")
    print(f"--- End report ---")

main()