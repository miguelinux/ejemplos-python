import tkinter as tk
from tkinter import ttk
import threading
import time

class MiAplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación con Threading")
        self.geometry("300x150")

        self.label = ttk.Label(self, text="Haz clic en el botón para iniciar la tarea.")
        self.label.pack(pady=10)

        self.progressbar = ttk.Progressbar(self, mode='indeterminate')
        self.progressbar.pack(pady=10)

        self.boton_iniciar = ttk.Button(self, text="Iniciar Tarea", command=self.iniciar_tarea)
        self.boton_iniciar.pack(pady=10)

        self.boton_detener = ttk.Button(self, text="Detener Tarea", state=tk.DISABLED, command=self.detener_tarea)
        self.boton_detener.pack(pady=10)

        self._detener_evento = threading.Event()
        self._hilo_trabajo = None

    def _tarea_larga(self):
        """Simula una tarea que lleva tiempo."""
        print("Tarea larga iniciada en un hilo.")
        for i in range(10):
            if self._detener_evento.is_set():
                print("Tarea larga detenida.")
                break
            time.sleep(1)
            print(f"Trabajando... {i+1}/10")
        print("Tarea larga finalizada.")
        self.after(0, self._tarea_finalizada) # Volver al hilo principal para actualizar la UI

    def iniciar_tarea(self):
        """Inicia la tarea en un hilo separado."""
        self.label.config(text="Tarea en progreso...")
        self.progressbar.start()
        self.boton_iniciar.config(state=tk.DISABLED)
        self.boton_detener.config(state=tk.NORMAL)
        self._detener_evento.clear()
        self._hilo_trabajo = threading.Thread(target=self._tarea_larga)
        self._hilo_trabajo.start()

    def detener_tarea(self):
        """Detiene la tarea en ejecución."""
        self._detener_evento.set()
        self.label.config(text="Deteniendo tarea...")
        self.boton_detener.config(state=tk.DISABLED)

    def _tarea_finalizada(self):
        """Se llama cuando la tarea ha finalizado (o se ha detenido)."""
        self.progressbar.stop()
        self.label.config(text="Tarea completada o detenida.")
        self.boton_iniciar.config(state=tk.NORMAL)
        self.boton_detener.config(state=tk.DISABLED)
        self._hilo_trabajo = None

if __name__ == "__main__":
    app = MiAplicacion()
    app.mainloop()
