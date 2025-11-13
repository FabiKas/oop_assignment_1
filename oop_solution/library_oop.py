class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        print("Error: No copies available!")
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        print(f"Error: All copies of '{self.title}' are already in the library.")
        return False


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        if book.borrow():
            self.borrowed_books.append(book.id)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        return False

    def return_book(self, book):
        if book.id not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        if book.return_book():
            self.borrowed_books.remove(book.id)
            print(f"{self.name} returned '{book.title}'")
            return True
        return False

    def display_borrowed_books(self, all_books):
        print(f"\n=== Books borrowed by {self.name} ===")
        if not self.borrowed_books:
            print("No books currently borrowed")
            return
        for book_id in self.borrowed_books:
            book = next((b for b in all_books if b.id == book_id), None)
            if book:
                print(f"- {book.title} by {book.author}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author, total_copies):
        self.books.append(Book(book_id, title, author, total_copies))
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        self.members.append(Member(member_id, name, email))
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        return next((b for b in self.books if b.id == book_id), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.id == member_id), None)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False
        return member.borrow_book(book)

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        return member.return_book(book)

    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        member.display_borrowed_books(self.books)

    def display_final_status(self):
        print("\nAll Borrowed Books:")
        for member in self.members:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"  {member.name} has '{book.title}'")
        print("\nAll Members and Their Books:")
        for member in self.members:
            print(f"\n{member.name} ({member.id}):")
            if member.borrowed_books:
                for book_id in member.borrowed_books:
                    book = self.find_book(book_id)
                    if book:
                        print(f"  - {book.title}")
            else:
                print("  (No books borrowed)")
        print("\n=== Available Books ===")
        for book in self.books:
            print(f"{book.title} by {book.author} - {book.available_copies} copies available")
