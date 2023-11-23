class Book:
    count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.count += 1

    def display(self):
        return self.title + ' by ' + self.author

    @staticmethod
    def book_long(length):
        return length > 200

    @classmethod
    def get_count(cls):
        return cls.count


book1 = Book("War and Peace", "Leo Tolstoy")
book2 = Book("Fathers and children", "Ivan Turgenev")
print(book1.display())
print(book2.display())
print(Book.book_long(300))
print(Book.book_long(150))
print(Book.get_count())
