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
    print("Boton precionado")


def on_key_press(event):
    if event.char == "a":
        print("Tecla \"a\" presionada")

def on_resize(event):
    print(f"La ventana ha sido redimensionada a {event.width}x{event.height}")

def on_mouse_move(event):
    print(f"Ratón movido a {event.x}, {event.y}")

def on_click_2(event):
    print(f"Botón {event.widget['text']} presionado")

def main():
    """
    Función principal
    """
    ventana = tk.Tk()

    ventana.title("Ejemplo Boton")

    boton = tk.Button(ventana, text="Presiona aquí")
    boton.pack()

    boton.bind("<Button-1>", on_click)

    ventana.bind("<KeyPress>", on_key_press)
    #ventana.bind("<Configure>", on_resize)
    ventana.bind("<Motion>", on_mouse_move)


    ventana.mainloop()



if __name__ == "__main__":
    main()

