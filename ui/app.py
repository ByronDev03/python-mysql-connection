import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("CRUD USUARIOS")
root.geometry("600x400")

tk.Label(root, text="Nombre").pack()

entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Button(root, text="Agregar").pack()

tabla = ttk.Treeview(root, columns=("ID", "Nombre"))

tabla.heading("#1", text="ID")
tabla.heading("#2", text="Nombre")

tabla.pack()
root.mainloop()