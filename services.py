from models import Book, Member
from storage import load_data, save_data


class LibraryError(Exception):
    """Base exception for all library-related issues."""


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class DuplicateBookError(LibraryError):
    pass


class DuplicateMemberError(LibraryError):
    pass


class BookUnavailableError(LibraryError):
    pass


class LibraryService:
    def __init__(self):
        self.data = load_data()

    def _save(self):
        save_data(self.data)

    def add_book(self, book):
        for existing_book in self.data["books"]:
            if existing_book["book_id"] == book.book_id:
                raise DuplicateBookError(f"Book with ID {book.book_id} already exists.")

        self.data["books"].append(book.to_dict())
        self._save()
        return book

    def add_member(self, member):
        for existing_member in self.data["members"]:
            if existing_member["member_id"] == member.member_id:
                raise DuplicateMemberError(f"Member with ID {member.member_id} already exists.")

        self.data["members"].append(member.to_dict())
        self._save()
        return member

    def get_all_books(self):
        return [Book.from_dict(book) for book in self.data["books"]]

    def get_all_members(self):
        return [Member.from_dict(member) for member in self.data["members"]]

    def search_books(self, query):
        term = query.lower()
        matching_books = []

        for book_data in self.data["books"]:
            book = Book.from_dict(book_data)
            if term in book.title.lower() or term in book.author.lower() or term in book.genre.lower():
                matching_books.append(book)

        return matching_books

    def borrow_book(self, member_id, book_id):
        member_data = self._find_member_data(member_id)
        book_data = self._find_book_data(book_id)

        if book_data["quantity"] <= 0:
            raise BookUnavailableError(f"Book '{book_id}' is currently unavailable.")

        if book_id in member_data["borrowed_books"]:
            raise BookUnavailableError("This member has already borrowed this book.")

        book_data["quantity"] -= 1
        member_data["borrowed_books"].append(book_id)
        self._save()
        return Book.from_dict(book_data)

    def return_book(self, member_id, book_id):
        member_data = self._find_member_data(member_id)
        book_data = self._find_book_data(book_id)

        if book_id not in member_data["borrowed_books"]:
            raise BookNotFoundError("This member did not borrow the requested book.")

        member_data["borrowed_books"].remove(book_id)
        book_data["quantity"] += 1
        self._save()
        return Book.from_dict(book_data)

    def _find_member_data(self, member_id):
        for member in self.data["members"]:
            if member["member_id"] == member_id:
                return member
        raise MemberNotFoundError(f"Member with ID {member_id} was not found.")

    def _find_book_data(self, book_id):
        for book in self.data["books"]:
            if book["book_id"] == book_id:
                return book
        raise BookNotFoundError(f"Book with ID {book_id} was not found.")

    def get_member_borrowed_books(self, member_id):
        member_data = self._find_member_data(member_id)
        borrowed = []

        for book_data in self.data["books"]:
            if book_data["book_id"] in member_data["borrowed_books"]:
                borrowed.append(Book.from_dict(book_data))

        return borrowed
