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

variable_control = None

def mostrar_seleccion():
    print("Opción seleccinada", variable_control.get())

def main():
    """
    Función principal
    """
    ventana = tk.Tk()

    ventana.title("Ejemplo Radioboton")

    global variable_control
    variable_control = tk.IntVar()

    #opcion1 = tk.Radiobutton(ventana, text="Opción 1")
    #opcion1 = tk.Radiobutton(ventana, text="Opción 1", font=("Arial",14),
    #            fg="blue", bg="lightgray")

    opcion1 = tk.Radiobutton(ventana, text="Opción 1",
                             variable=variable_control, value=1)
    opcion2 = tk.Radiobutton(ventana, text="Opción 2",
                             variable=variable_control, value=2)

    boton = tk.Button(ventana, text="Mostrar selección",
                      command=mostrar_seleccion)

    opcion1.pack()
    opcion2.pack()
    boton.pack()

    ventana.mainloop()



if __name__ == "__main__":
    main()

