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

    ventana.title("Mi ventana")

    #ventana.geometry("640x480+100+50")
    ventana.geometry("640x480")

    ventana.minsize(400,200)
    ventana.maxsize(800,600)

    #ventana.iconbitmap("icono.ico")
    #ventana.configure(bg="lightblue")

    #       .reisizable(X , Y)
    #ventana.reisizable(False, False)
    #ventana.attributes("-alpha",0.5)

    ventana.mainloop()



if __name__ == "__main__":
    main()

