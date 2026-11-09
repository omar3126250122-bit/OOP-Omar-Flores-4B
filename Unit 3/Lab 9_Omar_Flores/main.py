import tkinter as tk
from Models import user_model, product_model
from Controllers import Authentication_controller, Products_controller
from Views import Login_view


class System:
    def __init__(self):
        self.root = tk.Tk()

        # Llamar modelos, vistas y controladores
        self.Model = user_model.UserModel()
        self.Model_Products = product_model.ProductModel()

        self.View_Login = Login_view.LoginView(self.root)

        # El controlador de productos abre la ventana de inventario
        # (con el Combobox y el botón "Exportar Reporte").
        self.Controller_Products = Products_controller.ProductsController(
            self.Model_Products,
            self.root
        )

        # Al iniciar sesión correctamente se abre el inventario.
        self.Controller_Authentication = Authentication_controller.Authentication(
            self.Model,
            self.View_Login,
            abrir_productos=self.Controller_Products.abrir
        )

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.start()
