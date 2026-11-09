import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):
        self.root = root

        # PERSONALIZAR 1:
        # Cambia el título de la ventana.
        self.root.title("Sistema De Ingreso")

        # PERSONALIZAR 2:
        # Modifica el ancho y alto de la ventana.
        self.root.geometry("620x550")

        # PERSONALIZAR 3:
        # Cambia el color de fondo.
        self.root.configure(bg="#1F3A5F")

        self.root.resizable(False, False)

        # PERSONALIZAR 4:
        # Cambia el texto, la fuente y los colores del título.
        self.titulo = tk.Label(
            root,
            text="INGRESAR",
            font=("Arial", 20, "bold"),
            bg="#F4A261",
            fg="#1F3A5F",
            padx=20,
            pady=5
        )
        self.titulo.pack(pady=20)

        # PERSONALIZAR 5:
        # Modifica el texto y la apariencia de las etiquetas.
        self.lbl_email = tk.Label(
            root,
            text="Email:",
            font=("Arial", 12, "bold"),
            bg="#1F3A5F",
            fg="#FFFFFF"
        )
        self.lbl_email.pack()

        # PERSONALIZAR 6:
        # Cambia el ancho, la fuente y otros atributos del campo.
        self.entry_email = tk.Entry(
            root,
            width=45,
            font=("Arial", 12),
            bg="#F1F5F9"
        )
        self.entry_email.pack(pady=8, ipady=4)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña:",
            font=("Arial", 12, "bold"),
            bg="#1F3A5F",
            fg="#FFFFFF"
        )
        self.lbl_password.pack()

        # El atributo show oculta los caracteres al escribir.
        self.entry_password = tk.Entry(
            root,
            width=45,
            font=("Arial", 12),
            show="*",
            bg="#F1F5F9"
        )
        self.entry_password.pack(pady=8, ipady=4)

        # PERSONALIZAR 7:
        # Cambia el texto, color, tamaño y fuente del botón.
        self.btn_login = tk.Button(
            root,
            text="Ingresar",
            width=20,
            bg="#E76F51",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        # PERSONALIZAR 8:
        # Cambia el diseño del botón para abrir el registro.
        self.btn_register = tk.Button(
            root,
            text="Crear cuenta",
            width=20,
            bg="#2A9D8F",
            fg="white",
            font=("Arial", 10),
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)