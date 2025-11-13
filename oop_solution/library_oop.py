class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self, member_name=None):
        if self.available_copies > 0:
            self.available_copies -= 1
            if member_name:
                print(f"{member_name} borrowed '{self.title}'")
            else:
                print(f"Borrowed one copy of '{self.title}'.")
            return True
        print("Error: No copies available!")
        return False

    def return_book(self, member_name=None):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            if member_name:
                print(f"{member_name} returned '{self.title}'")
            else:
                print(f"Returned one copy of '{self.title}'.")
            return True
        print(f"Error: All copies of '{self.title}' are already in the library!")
        return False

    def __str__(self):
        return f"{self.title} by {self.author} - {self.available_copies} copies available"

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
        if book.borrow(self.name):
            self.borrowed_books.append(book.id)
            return True
        return False

    def return_book(self, book):
        if book.id not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        if book.return_book(self.name):
            self.borrowed_books.remove(book.id)
            return True
        return False

    def display_borrowed_books(self, books_list):
        print(f"\n=== Books borrowed by {self.name} ===")
        if not self.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in self.borrowed_books:
                for book in books_list:
                    if book.id == book_id:
                        print(f"- {book.title} by {book.author}")
                        break
