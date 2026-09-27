class library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_users(self,user):
        self.users.append(user)

    def add_book(self,book):
        self.books.append(book)

    def show_list_users(self):
        for i in self.users:
            print(f"{i.show_user_info()}\n")

    def show_list_books(self):
        for i in self.books:
            print(f"{i.show_info_book()}\n")

# h = library()
# h.add_book(Book("1","dsf","asda","asd"))
# h.show_list_books()