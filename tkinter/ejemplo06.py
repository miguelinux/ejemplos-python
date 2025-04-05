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

    ventana.title("Ejemplo Boton")

    boton = tk.Button(ventana, text="Presiona aquí")
    boton.config(fg="white", bg="green", font=("Arial", 12))
    boton.pack()

    etiqueta = tk.Label(ventana, text="Hola, soy un Label")
    etiqueta.pack()

    def boton_presionado():
        print("Boton precionado")
        etiqueta.config(text="boton precionado")


    boton.config(command=boton_presionado)

    ventana.mainloop()



if __name__ == "__main__":
    main()

