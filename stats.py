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
