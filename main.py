from stats import get_word_count


def main():
    book_path = "./books/frankenstein.txt"

    word_count = get_word_count(book_path)

    print(f"Found {word_count} total words")


main()
