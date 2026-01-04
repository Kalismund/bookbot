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


def get_character_count(book):
    book_text = get_book_text(book)
    character_count = {}

    for char in book_text:
        lower_char = char.lower()

        if lower_char in character_count:
            character_count[lower_char] += 1
        else:
            character_count[lower_char] = 1

    return character_count
