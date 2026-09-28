class Book:
    def __init__(self, book_id, title, author, genre, quantity=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["genre"],
            data.get("quantity", 1),
        )

    def __str__(self):
        return f"{self.book_id} - {self.title} by {self.author} ({self.genre})"


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books,
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["member_id"], data["name"], data["email"])
        member.borrowed_books = data.get("borrowed_books", [])
        return member

    def __str__(self):
        return f"{self.member_id} - {self.name} ({self.email})"
