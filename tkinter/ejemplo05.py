#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de una ventana
"""

import time
import tkinter as tk


def main():
    """
    Función principal
    """
    ventana = tk.Tk()

    ventana.title("Ejemplo Label")

    etiqueta = tk.Label(ventana, text="Hola, soy un Label")

    etiqueta.pack()

    def actualiza_hora():
        etiqueta.config(text=time.strftime("%H:%M:%S"))
        ventana.after(100, actualiza_hora)

    actualiza_hora()

    ventana.mainloop()



if __name__ == "__main__":
    main()

