# MIS 132 - April 30
# Book Class

class Book:
    """
    Simple book class.
    """
    BOOK_TYPES = ("Hardcover", "Paperback", "Ebook")

    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if booktype in Book.BOOK_TYPES:
            self.booktype = booktype
        else:
            print(f"Error: The '{booktype}' is not a valid type. ")
            print("The valid book types are: ")
            for types in Book.BOOK_TYPES:
                print(f"- {types}")
            print("Please use one of them.")

    def get_price(self):
        if hasattr(self, "discount"):
            return self.price - (self.price * self.discount)
        else:
            return self.price

    def set_discount(self, amount=0.1):
        self.discount = amount

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages and ${self.price}"


deep_work = Book("Deep Work", "Cal Newport", 300, 20, "Ebook")
digital_minimalism = Book("Digital Minimalism", "Cal Newport", 382,25, "Hardcover" )
print(deep_work)
print(digital_minimalism)
print("\n")

print(digital_minimalism.get_price())
digital_minimalism.set_discount(0.5)
print(digital_minimalism.get_price())

new_book = Book("Nineteen Eighty-Four", "George Orwell", 448, 25, "Hard cover")


