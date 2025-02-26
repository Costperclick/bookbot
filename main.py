def get_book_text(path):

    with open(path) as f:
        return f.read()
    
def words_count(text):

    words_list = text.split()
    words_count = len(words_list)

    return words_count 

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = words_count(book_text)
    print(f"{count} words found in the document")

main()

