class Book:
    def __init__(self, book_name, author, isbn):   
        self.book_name = book_name
        self.author = author
        self.isbn = isbn
     
    def display_book(self):
        print(self.book_name)
        print(self.author)
        print(self.isbn)

class Library:
    def __init__(self):   
        self.material = []
    
    def insert(self, book):
        self.material.append(book)
    
    def search_book(self, book_name):
        bookstore= []
        for book in self.material:
            if book.book_name == book_name:
                bookstore.append(book)
        return bookstore
    
    def search_author(self, author):
        bookstore= []
        for book in self.material:
            if book.author == author:
                bookstore.append(book)
        return bookstore
    
    def search_isbn(self, isbn):
        bookstore = []
        for book in self.material:
            if book.isbn == isbn:
               bookstore.append(book)
        return bookstore
    
def show_books(results):
    if results:
        for book in results:
            book.display_book()
    else:
        print("no")
 


def choice():
    lib = Library()
    while True:
       
        print("1. Add a book",'\n',"2. Search by book title",'\n',"3. Search by author",'\n',"4. Search by ISBN")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            book_name = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(book_name, author, isbn)
            lib.insert(book)
            print("Book added successfully!")
        elif choice == 2:
            book_name = input("Enter book title to search: ")
            show= lib.search_book(book_name)
            show_books(show)
        elif choice == 3:
            author = input("Enter author name to search: ")
            show = lib.search_author(author)
            show_books(show)
        elif choice == 4:
            isbn = input("Enter ISBN to search: ")
            show = lib.search_isbn(isbn)
            show_books(show)
         
        else:
            print("Invalid choice")
choice()

