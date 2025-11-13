from library_oop import Book

def test_book_class():
    print("=== TEST BOOK CLASS ===")
    
    book = Book(1, "Python Crash Course", "Eric Matthes", 3)
    print(book)

    book.borrow()
    print(book)

    book.borrow()
    book.borrow()
    print(book)

    book.borrow()
    print(book)

    book.return_book()
    print(book)

    book.return_book()
    book.return_book()
    print(book)

    book.return_book()
    print(book)

if __name__ == "__main__":
    test_book_class()
