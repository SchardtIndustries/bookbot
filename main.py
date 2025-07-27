def get_book_text(filepath):
     with open (filepath, 'r') as file:
        content = file.read()
        return content
def main():
    t = get_book_text("books/frankenstein.txt")
    from stats import count
    count(t)
    word_count = count(t)
    print (f"{word_count} words found in the document")

main()
