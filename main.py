import sys

from stats import get_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(get_report(sys.argv[1]))
    sys.exit(0)


main()
