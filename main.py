from stats import count
from stats import count_characters
from stats import sort_character_counts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open (filepath, 'r') as file:
        content = file.read()
        return content

def main():
    t = get_book_text(sys.argv[1])
    word_count = count(t)
    cc = count_characters(t)
    scc = sort_character_counts(cc)
    print ("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in scc:
        item["char"]
        item['num']
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
