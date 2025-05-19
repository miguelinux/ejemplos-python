import tkinter as tk
from tkinter import ttk
import time
import threading

def tarea_larga(barra_progreso, texto_resultado):
    """Simula una tarea que lleva tiempo."""
    total_iteraciones = 10
    for i in range(total_iteraciones + 1):
        time.sleep(0.5)  # Simula un trabajo
        porcentaje = (i / total_iteraciones) * 100
        barra_progreso['value'] = porcentaje
        # ¡Importante! Usar after para actualizar la interfaz desde el hilo principal
        barra_progreso.master.after(0, barra_progreso.update)
        texto_resultado.set(f"Progreso: {int(porcentaje)}%")
    texto_resultado.set("¡Tarea completada!")

def iniciar_tarea():
    """Inicia la tarea larga en un hilo separado."""
    barra = barra_progreso
    resultado = texto_resultado
    hilo = threading.Thread(target=tarea_larga, args=(barra, resultado))
    hilo.daemon = True  # El hilo terminará cuando la ventana principal se cierre
    hilo.start()
    boton_iniciar['state'] = tk.DISABLED  # Deshabilitar el botón mientras la tarea se ejecuta
    # Habilitar el botón nuevamente cuando la tarea finalice (se podría hacer de forma más robusta)
    root.after(int((10 * 0.5 + 1) * 1000), lambda: boton_iniciar.config(state=tk.NORMAL))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ejemplo con Hilos en Tkinter")

# Barra de progreso
barra_progreso = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
barra_progreso.pack(pady=10)

# Etiqueta para mostrar el resultado
texto_resultado = tk.StringVar()
etiqueta_resultado = ttk.Label(root, textvariable=texto_resultado)
etiqueta_resultado.pack(pady=5)
texto_resultado.set("Esperando...")

# Botón para iniciar la tarea
boton_iniciar = ttk.Button(root, text="Iniciar Tarea Larga", command=iniciar_tarea)
boton_iniciar.pack(pady=10)

root.mainloop()
