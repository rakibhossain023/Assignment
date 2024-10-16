class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"
book1 = Book("2024", "George Gylsye Ieth", 423)
print(book1.get_description())