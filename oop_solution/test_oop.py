from library_oop import Library

def test_library_system():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    library = Library()

    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)

    print("\n--- TEST 2: Registering Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")

    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)

    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    library.display_member_books(103)

    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)
    library.display_available_books()

    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)

    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)
    library.display_member_books(101)
    library.borrow_book(101, 3)

    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)
    library.return_book(102, 1)
    library.display_member_books(101)
    library.display_available_books()

    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)

    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)
    library.borrow_book(102, 3)
    library.display_member_books(102)

    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)
    library.borrow_book(101, 999)
    library.return_book(999, 1)
    library.display_member_books(999)

    print("\n--- TEST 14: Final Library Status ---")
    library.display_final_status()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_library_system()
