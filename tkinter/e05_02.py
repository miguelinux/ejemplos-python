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
ventana = None

def cambiar_color():
    global ventana
    color_seleccionado = variable_control.get()

    if color_seleccionado == 1:
        ventana.config(bg="red")
    elif color_seleccionado == 2:
        ventana.config(bg="blue")

def main():
    """
    Función principal
    """
    global ventana
    ventana = tk.Tk()

    ventana.title("Ejemplo Radioboton")

    global variable_control
    variable_control = tk.IntVar()

    #opcion1 = tk.Radiobutton(ventana, text="Opción 1")
    #opcion1 = tk.Radiobutton(ventana, text="Opción 1", font=("Arial",14),
    #            fg="blue", bg="lightgray")

    opcion1 = tk.Radiobutton(ventana, text="Rojo",
                             variable=variable_control, value=1,
                             command=cambiar_color)
    opcion2 = tk.Radiobutton(ventana, text="Azul",
                             variable=variable_control, value=2,
                             command=cambiar_color)


    opcion1.pack()
    opcion2.pack()

    ventana.mainloop()



if __name__ == "__main__":
    main()

