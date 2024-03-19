# Library Management System in SCRIPT

# Define a dictionary to store book information

books = []

# Function to add book to the library
def add_book(title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    


# Function to display all books in the library 
def display_books():
    if len(books) == 0:
        print("No books availbale in the library.")
    
    else:
        print("All Books in the Library:")
        for book in books:
            print("Title: ", book["title"])
            print("Author: ", book["author"])
            print("Year: ", book["year"])
            print()
            
#  Function to list all  books by specific author        
def list_books_by_author(author_name):
    author_books = []
    for book in books:
        if book["author"].lower() == author_name.lower():
            author_books.append(book)
    if len(author_books) == 0:
        print("No books found for author: ", author_name)
    else:
        print("Books by Author: ", author_name)
        for book in author_books:
            print("Title: ", book["title"])
            print("Year: ", book["year"])
            print()
            
            
            
# Main Program
def main():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. List All Books by Author")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the year of publication: ")
            add_book(title, author, year)
            print("Book added successfully!")
        
        elif choice == "2":
            display_books()
            
        elif choice == "3":
            author_name = input("Enter the author's name: ")
            list_books_by_author(author_name)
            
        elif choice == "4":
            print("Exiting the program.....")
            break
        
        else:
            print("Invalid choice. Try again.....")
            
# Run the main program
main()