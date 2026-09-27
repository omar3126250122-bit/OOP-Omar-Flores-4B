class Book:
    def __init__(self,id_book,title,author,editorial):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.editorial = editorial
        self.available = True

    def show_info_book(self):
        return f"ID Book: {self.id_book}\nTitle:{self.title}\nAuthor:{self.author}\nEditorial: {self.editorial}\nAvailable:{self.available}"