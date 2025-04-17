#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de una ventana
"""
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo Notebook")

# Crear el widget Notebook
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill='both')

# Crear los frames para cada pestaña
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

# Agregar widgets a la primera pestaña
etiqueta1 = ttk.Label(frame1, text="Contenido de la Pestaña 1", padding=10)
etiqueta1.pack()
boton1 = ttk.Button(frame1, text="Botón en Pestaña 1")
boton1.pack(pady=5)

# Agregar widgets a la segunda pestaña
etiqueta2 = ttk.Label(frame2, text="Contenido de la Pestaña 2", padding=10)
etiqueta2.pack()
entrada2 = ttk.Entry(frame2)
entrada2.pack(pady=5)

# Agregar widgets a la tercera pestaña
etiqueta3 = ttk.Label(frame3, text="Contenido de la Pestaña 3", padding=10)
etiqueta3.pack()
checkbutton3 = ttk.Checkbutton(frame3, text="Opción en Pestaña 3")
checkbutton3.pack(pady=5)

# Añadir los frames como pestañas al Notebook
notebook.add(frame1, text='Pestaña 1')
notebook.add(frame2, text='Pestaña 2')
notebook.add(frame3, text='Pestaña 3')

ventana.mainloop()
