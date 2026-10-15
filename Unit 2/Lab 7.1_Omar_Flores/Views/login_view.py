import os  # 1. Importa os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Model.login_model import User
from .home_view import DashboardVentana


class LoginVentana:
    """Ventana de inicio de sesión."""

    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        # Construir la interfaz
        self._crear_interfaz()

    def _crear_interfaz(self):
        # --- CARGAR E INSERTAR EL ICONO DE FORMA SEGURA ---
        try:
            # Obtiene la ruta absoluta de la carpeta actual (Views)
            base_dir = os.path.dirname(os.path.abspath(__file__))
            # Si icon.jpg está en la misma carpeta Views:
            icon_path = os.path.join(base_dir, "../aseets/local-area.png")

            img_pil = Image.open(icon_path)
            img_pil = img_pil.resize((70, 70), Image.Resampling.LANCZOS)
            self.img_icon = ImageTk.PhotoImage(img_pil)
            
            lbl_icono = tk.Label(self.root, image=self.img_icon)
            lbl_icono.pack(pady=(20, 0))
        except Exception as e:
            print(f"Error detallado al cargar el icono: {e}")

        # Resto de tus componentes...
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=15)
        # ... (continúa el resto de tu código de la vista)

        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)

        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar", 
            font=("Helvetica", 11, "bold"),
            bg="#2196F3", 
            fg="white", 
            cursor="hand2",
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=25)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.autenticar()

        if datos_usuario:
            messagebox.showinfo("Bienvenido", f"¡Hola {datos_usuario['nombre']}! Acceso concedido.")
            self._abrir_dashboard(datos_usuario['nombre'])
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()