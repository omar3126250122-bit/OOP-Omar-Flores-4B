import tkinter as tk
from Models import user_model
from Controllers import Authentication_controller
from Views import Login_view


class System:
    def __init__(self):
        self.root = tk.Tk()

        #Llamar modelos, vistas y controladores pendientes
        self.Model = user_model.UserModel()
        self.View_Login = Login_view.LoginView(self.root)
        self.Controller_Authentication = Authentication_controller.Authentication(self.Model,self.View_Login)
        


    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = System()
    app.start()
