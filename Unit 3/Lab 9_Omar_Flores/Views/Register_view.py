import tkinter as tk
from tkinter import messagebox

class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        # PERSONALIZAR 1:
        # Cambia el título de la ventana.
        self.ventana.title("Registro De Usuarios")

        # PERSONALIZAR 2:
        # Modifica las dimensiones de la ventana.
        self.ventana.geometry("620x600")

        # PERSONALIZAR 3:
        # Cambia el color de fondo.
        self.ventana.configure(bg="#59A9E6")

        self.ventana.resizable(False, False)

        # Mantiene la ventana asociada a la principal.
        self.ventana.transient(root)
        self.ventana.grab_set()

        # PERSONALIZAR 4:
        # Cambia el título, la fuente y sus colores.
        self.titulo = tk.Label(
            self.ventana,
            text="CREAR CUENTA",
            font=("Arial", 20, "bold"),
            bg="#F09783",
            fg="#000001",
            padx=20,
            pady=5
        )
        self.titulo.pack(pady=18)

        # PERSONALIZAR 5:
        # Modifica el texto y estilo de las etiquetas.
        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#59A9E6",
            font=("Arial", 12, "bold")
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=45,
            font=("Arial", 12)
        )
        self.entry_nombre.pack(pady=6, ipady=3)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Email:",
            bg="#59A9E6",
            font=("Arial", 12, "bold")
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=45,
            font=("Arial", 12)
        )
        self.entry_email.pack(pady=6, ipady=3)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg="#59A9E6",
            font=("Arial", 12, "bold")
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=45,
            show="*",
            font=("Arial", 12)
        )
        self.entry_password.pack(pady=6, ipady=3)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#59A9E6",
            font=("Arial", 12, "bold")
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=45,
            show="*",
            font=("Arial", 12)
        )
        self.entry_confirmar.pack(pady=6, ipady=3)

        # PERSONALIZAR 6:
        # Cambia el texto, color, fuente y tamaño del botón.
        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar",
            width=20,
            bg="#27AE60",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=15)

        # Botón para cancelar el registro.
        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=20,
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()