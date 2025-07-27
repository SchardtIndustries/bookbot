from stats import count
from stats import count_characters
def get_book_text(filepath):
     with open (filepath, 'r') as file:
        content = file.read()
        return content

def main():
    t = get_book_text("books/frankenstein.txt")
    word_count = count(t)
    cc = count_characters(t)
    print (f"{word_count} words found in the document")
    print (cc)
main()
