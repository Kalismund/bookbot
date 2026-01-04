def get_book_text(path):
    file_contents = ""

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def get_word_count(book):
    count = 0

    text = get_book_text(book)
    word_list = text.split()
    count = len(word_list)

    return count


def main():
    book_path = "./books/frankenstein.txt"

    word_count = get_word_count(book_path)

    print(f"Found {word_count} total words")


main()
