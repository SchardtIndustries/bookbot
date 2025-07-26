def get_book_text(filepath):
     with open (filepath, 'r') as file:
        content = file.read()
        return content

def main():
    t = get_book_text("books/frankenstein.txt")
    print(t)

main()
