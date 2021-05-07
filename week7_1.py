# MIS 132 - May 7
# Book, Magazine, Newspaper - Publication, Periodicals Classes - Inheritance

class Publication:

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price


class Periodicals(Publication):

    def __init__(self, title, price, period, publisher):
        Publication.__init__(self, title, price)
        self.period = period
        self.publisher = publisher

    def get_period(self):
        return f"The publication is a {self.period} publication."

    def get_price(self):
        return f"The issue is {self.price} dollars."


class Book(Publication):

    def __init__(self, title, price, author, pages):
        #super().__init__(self, title, price)
        Publication.__init__(self, title, price)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages - ${self.price}"

    def get_title(self):
        return f"The name of the book is {self.title}"


class Magazine(Periodicals):
    """
    A simple magazine class.
    """
    def __init__(self, title, publisher, price, period):
        Periodicals.__init__(self, title, price, period, publisher)

    def __str__(self):
        return f"{self.title} is a {self.period} magazine and published by {self.publisher}."

    def get_period(self):
        return f"{self.title} magazine is publishing by {self.publisher} in {self.period} periods."

    def get_price(self):
        return f"The magazine's one issue is {self.price} dollars."


class Newspaper(Periodicals):

    def __init__(self, title, publisher, price, period):
        Periodicals.__init__(self, title, price, period, publisher)


book1 = Book("Nineteen Eight-Four", 10, "George Orwell", 340)
#print(book1)

magazine1 = Magazine("The New Yorker", "Conde Nast", 6, "weekly")
#print(magazine1)

newspaper1 = Newspaper("The New York Times", "The NY Times Company", 4, "daily")

#print(book1.get_title())
#print(newspaper1.get_period())
#print(newspaper1.get_title())

print(magazine1.get_period())
print(magazine1.get_price())
