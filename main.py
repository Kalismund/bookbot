from stats import get_character_count, get_word_count


def main():
    book_path = "./books/frankenstein.txt"

    word_count = get_word_count(book_path)
    character_count = get_character_count(book_path)

    print(f"Found {word_count} total words")
    print(character_count)


main()
