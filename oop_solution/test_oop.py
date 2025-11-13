from library_oop import Book, Member

def test_book_and_member():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - CLASS TEST")
    print("=" * 60)

    print("\n--- TEST 1: Adding Books ---")
    book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
    book2 = Book(2, "Clean Code", "Robert Martin", 2)
    book3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    book4 = Book(4, "Design Patterns", "Gang of Four", 2)
    books = [book1, book2, book3, book4]
    for book in books:
        print(f"Book '{book.title}' added successfully!")

    print("\n--- TEST 2: Registering Members ---")
    member1 = Member(101, "Alice Smith", "alice@email.com")
    member2 = Member(102, "Bob Jones", "bob@email.com")
    member3 = Member(103, "Carol White", "carol@email.com")
    members = [member1, member2, member3]
    for member in members:
        print(f"Member '{member.name}' registered successfully!")

    print("\n--- TEST 3: Display Available Books ---")
    print("\n=== Available Books ===")
    for book in books:
        print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    print("\n--- TEST 4: Successful Borrowing ---")
    member1.borrow_book(book1)
    member1.borrow_book(book2)
    member2.borrow_book(book1)

    print("\n--- TEST 5: Display Member's Books ---")
    for member in members:
        member.display_borrowed_books(books)

    print("\n--- TEST 6: Available Books After Borrowing ---")
    print("\n=== Available Books ===")
    for book in books:
        print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    print("\n--- TEST 7: Borrowing Last Copy ---")
    member3.borrow_book(book3)
    print("\n=== Available Books ===")
    for book in books:
        print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    member2.borrow_book(book3)

    print("\n--- TEST 9: Borrowing Limit Test ---")
    member1.borrow_book(book4)
    member1.display_borrowed_books(books)
    member1.borrow_book(book3)

    print("\n--- TEST 10: Returning Books ---")
    member1.return_book(book1)
    member2.return_book(book1)
    member1.display_borrowed_books(books)
    print("\n=== Available Books ===")
    for book in books:
        print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    print("\n--- TEST 11: Attempting Invalid Return ---")
    member2.return_book(book2)

    print("\n--- TEST 12: Return and Re-borrow ---")
    member3.return_book(book3)
    member2.borrow_book(book3)
    member2.display_borrowed_books(books)

    print("\n--- TEST 13: Error Handling ---")
    fake_member = Member(999, "Ghost", "ghost@email.com")
    fake_member.borrow_book(book1)
    member1.borrow_book(Book(999, "Nonexistent", "Nobody", 1))
    fake_member.return_book(book1)
    fake_member.display_borrowed_books(books)

    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Members and Their Books:")
    for member in members:
        member.display_borrowed_books(books)

    print("\n=== Available Books ===")
    for book in books:
        print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_and_member()
