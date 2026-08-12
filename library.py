# Library Management System
# Python Mini Project using OOP


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


    def display(self):
        status = "Available" if self.available else "Issued"

        print("--------------------------------")
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Status  :", status)



class Library:

    def __init__(self):
        self.books = []              # List
        self.issued_books = {}       # Dictionary
        self.authors = set()         # Set

        self.load_books()


    # Add Book
    def add_book(self):

        try:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")


            book = Book(book_id, title, author)

            self.books.append(book)
            self.authors.add(author)


            self.save_books()

            print("Book added successfully!")

        except ValueError:
            print("Invalid Book ID!")



    # Display Books
    def display_books(self):

        if len(self.books) == 0:
            print("No books available")

        else:
            for book in self.books:
                book.display()



    # Search Book
    def search_book(self):

        keyword = input("Enter book title to search: ")

        found = False

        for book in self.books:

            if keyword.lower() in book.title.lower():
                book.display()
                found = True


        if not found:
            print("Book not found")



    # Issue Book
    def issue_book(self):

        try:
            book_id = int(input("Enter Book ID to issue: "))


            for book in self.books:

                if book.book_id == book_id:

                    if book.available:

                        student = input("Enter Student Name: ")

                        book.available = False

                        self.issued_books[book_id] = student

                        print("Book issued successfully")

                        return

                    else:
                        print("Book already issued")
                        return


            print("Book not found")


        except ValueError:
            print("Invalid ID")



    # Return Book
    def return_book(self):

        try:
            book_id = int(input("Enter Book ID to return: "))


            if book_id in self.issued_books:

                for book in self.books:

                    if book.book_id == book_id:
                        book.available = True


                del self.issued_books[book_id]

                print("Book returned successfully")


            else:
                print("Book is not issued")


        except ValueError:
            print("Invalid ID")



    # Display Issued Books
    def issued_list(self):

        if len(self.issued_books)==0:
            print("No issued books")

        else:

            print("\nIssued Books")

            for book,student in self.issued_books.items():

                print(
                    "Book ID:",
                    book,
                    "Issued To:",
                    student
                )



    # Save data to file
    def save_books(self):

        file = open("books.txt","w")

        for book in self.books:

            file.write(
                f"{book.book_id},{book.title},{book.author},{book.available}\n"
            )

        file.close()



    # Load data from file
    def load_books(self):

        try:

            file=open("books.txt","r")

            for line in file:

                data=line.strip().split(",")

                book=Book(
                    int(data[0]),
                    data[1],
                    data[2]
                )

                book.available = data[3]=="True"

                self.books.append(book)


            file.close()


        except FileNotFoundError:

            pass




# Main Program


library = Library()


while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")

    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Issued Books")
    print("7. Exit")


    try:

        choice=int(input("Enter your choice: "))


        if choice==1:
            library.add_book()


        elif choice==2:
            library.display_books()


        elif choice==3:
            library.search_book()


        elif choice==4:
            library.issue_book()


        elif choice==5:
            library.return_book()


        elif choice==6:
            library.issued_list()


        elif choice==7:

            print("Thank you!")
            break


        else:
            print("Invalid choice!")


    except ValueError:

        print("Please enter numbers only!")