class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author


class PaperBook(Book):

    def __init__(self, name, author, pages: int, ):
        super().__init__(name, author)
        super().__repr__()
        self.pages = pages

    def __str__(self):
        return f"Книга {PaperBook.name}. Автор {self.author}. Количество страниц {self.pages}"

#    def __repr__(self):
#        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        name = PaperBook.name
        self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        author = PaperBook.author
        self._author = author


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


book_1 = Book('Полтава', 'А.С.Пушкин')
print(book_1)
book_2 = PaperBook(book_1.name, book_1.author, 88)
print(book_2.__dict__)
book_2.name = 'Метель'
print(book_2.__dict__)
print(book_2)
