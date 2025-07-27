from stats import count
from stats import count_characters
from stats import sort_character_counts

def get_book_text(filepath):
     with open (filepath, 'r') as file:
        content = file.read()
        return content

def main():
    t = get_book_text("books/frankenstein.txt")
    word_count = count(t)
    cc = count_characters(t)
    scc = sort_character_counts(cc)
    print ("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in scc:
        item["char"]
        item['num']
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
