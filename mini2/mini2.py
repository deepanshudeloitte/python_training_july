from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"{book.title} is not available for borrowing")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

    def borrowed_book_list(self):
        if self.borrowed_books:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(book)
        else:
            print(f"{self.name} has not borrowed any books.")


class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' has been removed from the library.")
        else:
            print(f"Book '{book.title}' is not present in the library.")

    def display_all_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("The library has no books.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

    def display_overdue_books(self):
        current_date = datetime.now()
        overdue_books = []
        for student in self.students:
            for book in student.borrowed_books:
                due_date = book.borrow_date + timedelta(days=14)  # Assuming the borrowing period is 14 days
                if current_date > due_date:
                    overdue_books.append(book)
        if overdue_books:
            print("Overdue books:")
            for book in overdue_books:
                print(book)
        else:
            print("No books are currently overdue.")

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' with ID '{student.student_id}' has been added to the library.")


# Testing the Library Management System
library = Library()

# Adding books to the library
book1 = Book("Python Crash Course", "Eric Matthes", "978-1-59327-603-4")
book2 = Book("Clean Code", "Robert C. Martin", "978-0-13-235088-4")
book3 = Book("The Pragmatic Programmer", "Andrew Hunt, David Thomas", "978-0-13-595705-9")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Adding a student
student1 = Student("John Smith", "2021001")
library.add_student(student1)

# Displaying all books in the library
library.display_all_books()

# Displaying available books
library.display_available_books()

# Student borrowing a book
student1.borrow_book(book1)

# Displaying borrowed books by a student
student1.borrowed_book_list()

# Displaying available books after a book has been borrowed
library.display_available_books()

# Returning a book by a student
student1.return_book(book1)

# Displaying available books after a book has been returned
library.display_available_books()

# Displaying overdue books
library.display_overdue_books()
