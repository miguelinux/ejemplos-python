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
ventana.title("Ejemplo LabelFrame")

# Crear el LabelFrame
grupo = ttk.LabelFrame(ventana, text="Información del Usuario")
grupo.pack(padx=10, pady=10)

# Agregar widgets dentro del LabelFrame
etiqueta_nombre = ttk.Label(grupo, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)
entrada_nombre = ttk.Entry(grupo)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

etiqueta_edad = ttk.Label(grupo, text="Edad:")
etiqueta_edad.grid(row=1, column=0, padx=5, pady=5)
entrada_edad = ttk.Entry(grupo)
entrada_edad.grid(row=1, column=1, padx=5, pady=5)

ventana.mainloop()

