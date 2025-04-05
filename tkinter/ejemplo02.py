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

def main():
    """
    Función principal
    """
    ventana = tk.Tk()

    ventana.title("Mi ventana 2")

    ventana.geometry("640x480")
    ventana.configure(bg="lightblue")

    frame1 = tk.Frame(ventana)
    frame1.configure(width=300, height=200, bg="red", bd=5)
    frame1.pack()

    frame2 = tk.Frame(frame1)
    frame2.configure(width=100, height=100, bg="blue", bd=5)
    frame2.pack()

    boton = tk.Button(frame1, text="Hola")
    boton.pack()



    ventana.mainloop()



if __name__ == "__main__":
    main()

