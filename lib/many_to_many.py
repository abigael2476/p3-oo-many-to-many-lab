class Author:
    _all = []

    def __init__(self, name):
        self.name = name
        Author._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Author name must be a string")
        self._name = value

    @classmethod
    def all(cls):
        return cls._all

    def contracts(self):
        # Return all contracts that involve this author
        return [contract for contract in Contract.all() if contract.author == self]

    def books(self):
        # Using Contract as the intermediary, return unique list of related books
        return list({contract.book for contract in self.contracts()})


    def sign_contract(self, book, date, royalties):
        # Create and return a new Contract object between self and book
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Return total royalties (sum of royalties of all contracts associated with author)
        return sum(contract.royalties for contract in self.contracts())


class Book:
    _all = []

    def __init__(self, title):
        self.title = title
        Book._all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Book title must be a string")
        self._title = value

    @classmethod
    def all(cls):
        return cls._all

    def contracts(self):
        # Return all contracts that involve this book
        return [contract for contract in Contract.all() if contract.book == self]

    def authors(self):
        # Using Contract as the intermediary, return unique list of related authors
        return list({contract.author for contract in self.contracts()})


class Contract:
    _all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def contracts_by_date(cls, date):
        # Return all contracts matching the exact date, sorted by date (though all same date)
        filtered_contracts = [contract for contract in cls.all() if contract.date == date]
        # Sorting seems redundant as date is same, but keep for potential extension
        return sorted(filtered_contracts, key=lambda c: c.date)
