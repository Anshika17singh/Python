import os

def menu():
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Search for a book by title")
    print("3. Display all books")
    print("4. Delete a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

        


# Task-1: Function to add a new book to the library (books.txt)
def add_book(title, author, publication_year):
    with open('books.txt', 'a') as file:
        file.write(f"{title},{author},{publication_year},Available\n")
    print(f"Book '{title}' added to the library.")

# Task-2: Function to search for a book by title
def search_book(title):
    with open('books.txt', 'r') as file:
        books = file.readlines()
        for book in books:
            book_details = book.strip().split(',')
            if book_details[0].lower() == title.lower():
                print(f"Book Found: Title: {book_details[0]}, Author: {book_details[1]}, Year: {book_details[2]}, Status: {book_details[3]}")
                return
        print(f"Book '{title}' not found.")

# Task-3: Function to display all books in the library
def display_books():
    with open('books.txt', 'r') as file:
        books = file.readlines()
        if not books:
            print("No books in the library.")
            return
        for book in books:
            book_details = book.strip().split(',')
            print(f"Title: {book_details[0]}, Author: {book_details[1]}, Year: {book_details[2]}, Status: {book_details[3]}")

# Task-4: Function to delete a book by title
def delete_book(title):
    with open('books.txt', 'r') as file:
        books = file.readlines()

    with open('books.txt', 'w') as file:
        found = False
        for book in books:
            book_details = book.strip().split(',')
            if book_details[0].lower() == title.lower():
                found = True
            else:
                file.write(book)
        
        if found:
            print(f"Book '{title}' has been deleted.")
        else:
            print(f"Book '{title}' not found.")

# Task-5: Function to borrow a book and mark it as borrowed
def borrow_book(title):
    with open('books.txt', 'r') as file:
        books = file.readlines()

    with open('books.txt', 'w') as file, open('borrowed_books.txt', 'a') as borrowed_file:
        found = False
        for book in books:
            book_details = book.strip().split(',')
            if book_details[0].lower() == title.lower() and book_details[3] == 'Available':
                book_details[3] = 'Borrowed'
                file.write(','.join(book_details) + '\n')
                borrowed_file.write(','.join(book_details) + '\n')
                found = True
            else:
                file.write(book)

        if found:
            print(f"Book '{title}' has been borrowed.")
        else:
            print(f"Book '{title}' is either not available or does not exist.")

# Task-6: Function to mark a book as returned
def return_book(title):
    with open('borrowed_books.txt', 'r') as file:
        borrowed_books = file.readlines()

    with open('books.txt', 'r') as file:
        books = file.readlines()

    with open('books.txt', 'w') as file, open('borrowed_books.txt', 'w') as borrowed_file:
        found = False
        for book in books:
            book_details = book.strip().split(',')
            if book_details[0].lower() == title.lower() and book_details[3] == 'Borrowed':
                book_details[3] = 'Available'
                file.write(','.join(book_details) + '\n')
                found = True
            else:
                file.write(book)

        for borrowed_book in borrowed_books:
            borrowed_book_details = borrowed_book.strip().split(',')
            if borrowed_book_details[0].lower() != title.lower():
                borrowed_file.write(borrowed_book)
        
        if found:
            print(f"Book '{title}' has been returned.")
        else:
            print(f"Book '{title}' was not borrowed or does not exist.")

# Task-7: Main program loop to manage the library system
def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            publication_year = input("Enter the publication year: ")
            add_book(title, author, publication_year)

        elif choice == '2':
            title = input("Enter the book title to search: ")
            search_book(title)

        elif choice == '3':
            display_books()

        elif choice == '4':
            title = input("Enter the book title to delete: ")
            delete_book(title)

        elif choice == '5':
            title = input("Enter the book title to borrow: ")
            borrow_book(title)

        elif choice == '6':
            title = input("Enter the book title to return: ")
            return_book(title)

        elif choice == '7':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Ensure books.txt and borrowed_books.txt exist before running the system
    if not os.path.exists('books.txt'):
        with open('books.txt', 'w') as file:
            pass
    if not os.path.exists('borrowed_books.txt'):
        with open('borrowed_books.txt', 'w') as file:
            pass

    main()