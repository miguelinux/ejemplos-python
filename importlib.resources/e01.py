import importlib.resources

# Supongamos que tienes un paquete llamado 'mi_paquete'
# y dentro de él un archivo llamado 'datos.txt'

# Para leer el contenido del archivo como texto:
try:
    contenido = importlib.resources.read_text('mi_paquete', 'datos.txt')
    print("Contenido del archivo (como texto):\n", contenido)
except FileNotFoundError:
    print("El archivo 'datos.txt' no se encontró dentro del paquete 'mi_paquete'.")
except ModuleNotFoundError:
    print("El paquete 'mi_paquete' no se encontró.")

print("-" * 20)

# Para leer el contenido del archivo como bytes:
try:
    contenido_bytes = importlib.resources.read_binary('mi_paquete', 'datos.txt')
    print("Contenido del archivo (como bytes):\n", contenido_bytes)
except FileNotFoundError:
    print("El archivo 'datos.txt' no se encontró dentro del paquete 'mi_paquete'.")
except ModuleNotFoundError:
    print("El paquete 'mi_paquete' no se encontró.")

print("-" * 20)

# También puedes obtener la ruta al archivo (útil para ciertas operaciones):
try:
    ruta_archivo = importlib.resources.path('mi_paquete', 'datos.txt')
    print(f"Ruta al archivo: {ruta_archivo}")
    # ¡Importante! La ruta devuelta por path() podría ser un objeto context manager.
    # Es recomendable usarlo dentro de un bloque 'with' para asegurar la limpieza.
    with ruta_archivo as path_obj:
        print(f"Ruta como objeto Path: {path_obj}")
except FileNotFoundError:
    print("El archivo 'datos.txt' no se encontró dentro del paquete 'mi_paquete'.")
except ModuleNotFoundError:
    print("El paquete 'mi_paquete' no se encontró.")
