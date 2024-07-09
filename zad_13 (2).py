
class Book:
    def __init__(self, author, title, publisher, date, binding):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        self.binding = binding

    def show_author(self):
        return self.author

    def show_title(self):
        return self.title

    def read(self):
        print("Włsaśnie czytasz {} autorstwa {}".format(self.title, self.author))

def sort(books):
        return sorted(books, key=lambda x: x.title)

books = [
    Book("George Orwell", "Rok 1984", "MUZA S.A", 1949, "miękka"),
    Book("Aaron Demski Bowden", "Książę wron", "Copernicus Corporation", 2012, "miękka"),
    Book("Andrzej Sapkowski", "Ostatnie Życzenie", "SuperNowa", 2014,"miękka"),
    Book("Bolesław Prus", "Lalka", "Greg", 1890, "twrada"),
    Book("Adam Mickiewicz", "Dziady cz.2", "Greg", 1823, "twarda")
    ]
books[0].read()

books_sorted = sort(books)
for book in books_sorted:
    print(book.show_title(), book.show_author())