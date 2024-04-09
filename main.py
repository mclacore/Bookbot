def main():
    # reads the book
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book_content = f.read()
        
    # counts the words
    word_count = len(book_content.split())
    lower_words = book_content.lower()

    # counts the letters
    letter_list = []
    letter_dict = {}
    letter_count = 0
    for letters in lower_words:
        alpha = "".join(char for char in letters if char.isalpha())
        letter_list.append(alpha)
        for letter in letter_list:
            letter_dict[letter] = 1

    # returns
    print(letter_dict)
    print(f"Book has {word_count} words.")


main()