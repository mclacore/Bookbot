def main():
    # reads the book
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book_content = f.read()
        
    # counts the words
    word_count = len(book_content.split())

    # counts the letters
    letter_dict = {}
    for letters in book_content:
        lower_words = letters.lower()
        if lower_words in letter_dict:
            letter_dict[lower_words] += 1
        else:
            letter_dict[lower_words] = 1

    # returns
    print(letter_dict)
    print(f"Book has {word_count} words.")


main()