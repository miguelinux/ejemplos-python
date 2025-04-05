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

    label_frame = tk.LabelFrame(ventana, text="Grupo de widgets", bg="yellow",
                                padx=10, pady=10)
    label_frame.configure(width=300, height=200)
    label_frame.pack()


    ventana.mainloop()



if __name__ == "__main__":
    main()

