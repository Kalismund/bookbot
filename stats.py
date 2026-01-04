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

        if not lower_char.isalpha():
            continue  # skip anything that's not a letter

        if lower_char in character_count:
            character_count[lower_char] += 1
        else:
            character_count[lower_char] = 1

    return character_count


def get_sorted_character_count(book):
    character_count = get_character_count(book)

    # Convert the dictionary into a list of dictionaries
    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "num": count})

    # Sort by count descending
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list


def get_report(book):
    header = "============ BOOKBOT ============"
    title = f"Analyzing book found at {book[2:]}..."
    sub_word_count = "----------- Word Count ----------"
    word_count = f"Found {get_word_count(book)} total words"
    sub_character_count = "--------- Character Count -------"

    sorted_chars = get_sorted_character_count(book)

    # Convert list of dicts into printable lines
    char_lines = [f"{item['char']}: {item['num']}" for item in sorted_chars]
    character_count = "\n".join(char_lines)

    footer = "============= END ==============="

    sections = [
        header,
        title,
        sub_word_count,
        word_count,
        sub_character_count,
        character_count,
        footer,
    ]

    return "\n".join(sections)
