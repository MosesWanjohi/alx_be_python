class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title}, {self.author}" 

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __int__(self):
        return self.file_size
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __int__(self):
        return self.page_count
    
class Library:
    def __init__(self, books):
        self.books = []
    
    def add_book(self, book):
        self.book = book.append(self.books)
    
    def list_books(self):
        return [{book} for book in self.books]
