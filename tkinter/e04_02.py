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

def on_click(event):
    print(f"Botón {event.widget['text']} presionado")

def main():
    """
    Función principal
    """
    ventana = tk.Tk()

    ventana.title("Ejemplo Boton")

    botones = [tk.Button(ventana, text=f"Hola {i}") for i in range(3)]

    for b in botones:
        b.pack()
        b.bind("<Button-1>", on_click)

    ventana.mainloop()



if __name__ == "__main__":
    main()

