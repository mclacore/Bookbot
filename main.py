from collections import Counter

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
    # letter_count = 0
    for letters in lower_words:
        alpha = "".join(char for char in letters if char.isalpha())
        letter_list.append(alpha)
        # for letter in letter_list:
        #     letter_count += 1
        #     letter_dict = dict.fromkeys(letter, letter_count)
    letter_dict = Counter(letter_list)

    # returns
    print(letter_dict)
    print(f"Book has {word_count} words.")


main()