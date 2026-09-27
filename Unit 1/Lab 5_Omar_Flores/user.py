class User:
    def __init__(self,id_user,name,password):
        self.id_user = id_user
        self.name = name
        self._password = password
        self.borrow = True

    def show_user_info(self):
        return f"ID User:{self.id_user}\nName User:{self.name}\nStatus: {self.borrow}"