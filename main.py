from models import Book, Member
from services import (
    BookNotFoundError,
    BookUnavailableError,
    DuplicateBookError,
    DuplicateMemberError,
    LibraryService,
    MemberNotFoundError,
)


def print_books(books):
    if not books:
        print("No books available.")
        return

    print("\nBooks:")
    for book in books:
        print(f"- {book}")


def print_members(members):
    if not members:
        print("No members registered.")
        return

    print("\nMembers:")
    for member in members:
        print(f"- {member}")


def add_book_flow(service):
    book_id = input("Enter book ID: ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    genre = input("Enter genre: ").strip()
    quantity = int(input("Enter quantity: ").strip())

    book = Book(book_id, title, author, genre, quantity)
    try:
        service.add_book(book)
        print("Book added successfully.")
    except DuplicateBookError as exc:
        print(f"Error: {exc}")


def add_member_flow(service):
    member_id = input("Enter member ID: ").strip()
    name = input("Enter member name: ").strip()
    email = input("Enter email: ").strip()

    member = Member(member_id, name, email)
    try:
        service.add_member(member)
        print("Member added successfully.")
    except DuplicateMemberError as exc:
        print(f"Error: {exc}")


def borrow_book_flow(service):
    member_id = input("Enter member ID: ").strip()
    book_id = input("Enter book ID: ").strip()

    try:
        book = service.borrow_book(member_id, book_id)
        print(f"Book borrowed successfully: {book.title}")
    except (MemberNotFoundError, BookNotFoundError, BookUnavailableError) as exc:
        print(f"Error: {exc}")


def return_book_flow(service):
    member_id = input("Enter member ID: ").strip()
    book_id = input("Enter book ID: ").strip()

    try:
        book = service.return_book(member_id, book_id)
        print(f"Book returned successfully: {book.title}")
    except (MemberNotFoundError, BookNotFoundError) as exc:
        print(f"Error: {exc}")


def search_books_flow(service):
    query = input("Enter search term: ").strip()
    books = service.search_books(query)
    print_books(books)


def show_borrowed_books(service):
    member_id = input("Enter member ID: ").strip()
    try:
        books = service.get_member_borrowed_books(member_id)
        print_books(books)
    except MemberNotFoundError as exc:
        print(f"Error: {exc}")


def main():
    service = LibraryService()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Add a member")
        print("3. List all books")
        print("4. List all members")
        print("5. Search books")
        print("6. Borrow a book")
        print("7. Return a book")
        print("8. View borrowed books")
        print("9. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book_flow(service)
        elif choice == "2":
            add_member_flow(service)
        elif choice == "3":
            print_books(service.get_all_books())
        elif choice == "4":
            print_members(service.get_all_members())
        elif choice == "5":
            search_books_flow(service)
        elif choice == "6":
            borrow_book_flow(service)
        elif choice == "7":
            return_book_flow(service)
        elif choice == "8":
            show_borrowed_books(service)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
