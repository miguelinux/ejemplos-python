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

vcheck1 = None
ventana = None
boton = None

def on_checkbutton_cambio():
    global vcheck1
    global boton
    if vcheck1.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

def main():
    """
    Función principal
    """
    global ventana
    global vcheck1
    global boton
    ventana = tk.Tk()

    ventana.title("Ejemplo Radioboton")

    vcheck1 = tk.BooleanVar()
    #vcheck2 = tk.BooleanVar()

    #check1 = tk.Checkbutton(ventana, text="Opcion 1")
    #check1 = tk.Checkbutton(ventana, text="Opción 1", font=("Arial",14),
                #fg="blue", bg="lightgray")

    check1 = tk.Checkbutton(ventana, text="Opcion 1", variable=vcheck1,
                            command=on_checkbutton_cambio)
    #check2 = tk.Checkbutton(ventana, text="Opcion 2", variable=vcheck2)

    boton = tk.Button(ventana, text="Boton", state="disabled")

    check1.pack()
    #check2.pack()
    boton.pack()


    ventana.mainloop()



if __name__ == "__main__":
    main()

