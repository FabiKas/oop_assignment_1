Project Overview:

This project is to show the difference between a procedural and object-orientated programming. With a small code for a library. Where you have 3 Classes (Books, Members and Library), with them you can add books and members, borrow and return books with members, be keen about how many copies are still in stock. And the code also makes some error handling with unavailible books, invalid returns or borrowing limits.

The primary goal of this project is to provide a clear, maintainable OOP design while retaining all the functionality of a classic library system.

Project Structure:

We have two folders. One with the code of the procedural approach and the other with the oop approach. Each folder has one python file with the code for the classes and one file for the tests.

Class: Book
Attributes:
- id – Unique identifier
- title
- author
- total_copies – Total number of copies in the library
- available_copies – Current available copies

Methods:
- borrow() – Decreases the available_copies if they are available and prints an error if none left
- return_book() – Increases the available_copies when they are borrowed and prints an error if all copies are in the library

Class: Member
Attributes:
- id
- name
- email
- borrowed_books – List of book IDs currently borrowed by the member

Methods:
- borrow_book(book) – Borrow a book, with a  borrowing limit of 3 and prints the status
- return_book(book) – Return a already borrowed book and prints the status
- display_borrowed_books(all_books) – Lists all borrowed books

Class: Library
Attributes:
- books – List of all Book objects
- members – List of all Member objects

Methods:
- add_book(book_id, title, author, total_copies) – Adds a new book to the library
- add_member(member_id, name, email) – Registers a new member
- find_book(book_id) – Returns a Book object by ID
- find_member(member_id) – Returns a Member object by ID
- borrow_book(member_id, book_id) – Processes borrowing of a book for a member
- return_book(member_id, book_id) – Processes returning of a book for a member
- display_available_books() – Lists all books with at least one available copy
- display_member_books(member_id) – Lists all books borrowed by a member
- display_final_status() – Prints all borrowed books, member details, and available books


Testing

The test is in the test_oop file
The test covers:

Basic Operations:
- Add books and members
- Borrow and return books
- Display available books
- Display books borrowed by members

Edge Cases:
- Borrow books when no copies are available
- Borrow more than 3 books
- Returning books that are not borrowed
- Try actions with non-existent books or members