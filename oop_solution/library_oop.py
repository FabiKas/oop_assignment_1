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
