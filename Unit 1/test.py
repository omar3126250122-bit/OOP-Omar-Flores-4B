from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application")
root.geometry("640x480")
root.minsize(320, 240)

ttk.Label(root, text="Hello").pack(padx=20, pady=20)

root.mainloop()