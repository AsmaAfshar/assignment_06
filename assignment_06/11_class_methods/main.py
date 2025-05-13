

class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.total_books += 1  # Increment the total_books count each time a new book is created

    @classmethod
    def increase_book_count(cls):
        cls.total_books += 1  # Increment the class variable total_books

    @classmethod
    def get_total_books(cls):
        return cls.total_books  # Return the current total count of books

#Instance Method (__str__): Provides a string representation of the book instance, useful for printing book details
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Example usage
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

print(book1)  # Output: '1984' by George Orwell, 328 pages
print(book2)  # Output: 'To Kill a Mockingbird' by Harper Lee, 281 pages

print("Total books created:", Book.get_total_books())  # Output: Total books created: 2

# Adding a new book using the class method
Book.increase_book_count()
print("Total books created after increase:", Book.get_total_books())  # Output: Total books created after increase: 3
