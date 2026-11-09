import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class ProductsView:

    # Opciones del menú desplegable de exportación.
    FORMATOS = ("CSV", "TXT", "JSON", "PDF")

    def __init__(self, root, nombre_usuario=""):
        self.ventana = tk.Toplevel(root)

        self.ventana.title("Inventario De Productos")
        self.ventana.geometry("820x640")
        self.ventana.configure(bg="#1F3A5F")
        self.ventana.resizable(False, False)

        # ---------- Título ----------
        self.titulo = tk.Label(
            self.ventana,
            text="PRODUCTOS",
            font=("Arial", 20, "bold"),
            bg="#F4A261",
            fg="#1F3A5F",
            padx=20,
            pady=5
        )
        self.titulo.pack(pady=(15, 5))

        self.lbl_usuario = tk.Label(
            self.ventana,
            text=f"Sesión: {nombre_usuario}" if nombre_usuario else "",
            font=("Arial", 10),
            bg="#1F3A5F",
            fg="#FFFFFF"
        )
        self.lbl_usuario.pack()

        # ---------- Formulario de registro ----------
        self.frame_form = tk.Frame(self.ventana, bg="#1F3A5F")
        self.frame_form.pack(pady=10)

        tk.Label(
            self.frame_form, text="Nombre:",
            font=("Arial", 11, "bold"), bg="#1F3A5F", fg="#FFFFFF"
        ).grid(row=0, column=0, padx=6, sticky="w")

        tk.Label(
            self.frame_form, text="Precio:",
            font=("Arial", 11, "bold"), bg="#1F3A5F", fg="#FFFFFF"
        ).grid(row=0, column=1, padx=6, sticky="w")

        tk.Label(
            self.frame_form, text="Stock:",
            font=("Arial", 11, "bold"), bg="#1F3A5F", fg="#FFFFFF"
        ).grid(row=0, column=2, padx=6, sticky="w")

        self.entry_nombre = tk.Entry(
            self.frame_form, width=30, font=("Arial", 11), bg="#F1F5F9"
        )
        self.entry_nombre.grid(row=1, column=0, padx=6, ipady=3)

        self.entry_precio = tk.Entry(
            self.frame_form, width=12, font=("Arial", 11), bg="#F1F5F9"
        )
        self.entry_precio.grid(row=1, column=1, padx=6, ipady=3)

        self.entry_stock = tk.Entry(
            self.frame_form, width=10, font=("Arial", 11), bg="#F1F5F9"
        )
        self.entry_stock.grid(row=1, column=2, padx=6, ipady=3)

        self.btn_guardar = tk.Button(
            self.frame_form,
            text="Registrar producto",
            bg="#2A9D8F",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.grid(row=1, column=3, padx=10)

        # ---------- Controles de exportación ----------
        self.frame_export = tk.Frame(self.ventana, bg="#1F3A5F")
        self.frame_export.pack(pady=8)

        tk.Label(
            self.frame_export, text="Formato:",
            font=("Arial", 11, "bold"), bg="#1F3A5F", fg="#FFFFFF"
        ).pack(side="left", padx=6)

        # Combobox de solo lectura con los 4 formatos.
        self.combo_formato = ttk.Combobox(
            self.frame_export,
            values=self.FORMATOS,
            state="readonly",
            width=10,
            font=("Arial", 11)
        )
        self.combo_formato.current(0)
        self.combo_formato.pack(side="left", padx=6)

        self.btn_exportar = tk.Button(
            self.frame_export,
            text="Exportar Reporte",
            bg="#E76F51",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        self.btn_exportar.pack(side="left", padx=10)

        # ---------- Tabla de productos ----------
        self.frame_tabla = tk.Frame(self.ventana, bg="#1F3A5F")
        self.frame_tabla.pack(fill="both", expand=True, padx=20, pady=(5, 20))

        columnas = ("id", "nombre", "precio", "stock")

        self.tabla = ttk.Treeview(
            self.frame_tabla, columns=columnas, show="headings", height=14
        )
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("stock", text="Stock")

        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("nombre", width=380, anchor="w")
        self.tabla.column("precio", width=120, anchor="e")
        self.tabla.column("stock", width=90, anchor="center")

        scroll = ttk.Scrollbar(
            self.frame_tabla, orient="vertical", command=self.tabla.yview
        )
        self.tabla.configure(yscrollcommand=scroll.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.entry_nombre.focus_set()

    # ---------- Datos del formulario ----------
    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        precio = self.entry_precio.get().strip()
        stock = self.entry_stock.get().strip()

        return nombre, precio, stock

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        self.entry_nombre.focus_set()

    # ---------- Exportación ----------
    def obtener_formato(self):
        return self.combo_formato.get()

    def pedir_ruta_guardado(self, formato, extension):
        # Cuadro "Guardar como". Devuelve "" si el usuario cancela.
        return filedialog.asksaveasfilename(
            parent=self.ventana,
            title=f"Guardar reporte {formato}",
            initialfile="reporte_productos",
            defaultextension=extension,
            filetypes=[(f"Archivo {formato}", f"*{extension}")]
        )

    # ---------- Tabla ----------
    def cargar_tabla(self, productos):
        self.tabla.delete(*self.tabla.get_children())

        for id_, nombre, precio, stock in productos:
            self.tabla.insert(
                "",
                tk.END,
                values=(id_, nombre, f"${float(precio):,.2f}", stock)
            )

    # ---------- Mensajes y cierre ----------
    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)

    def cerrar(self):
        self.ventana.destroy()
