import logging

class SoloErroresFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('mi_modulo')

# Handler para la consola (mostrar solo errores)
console_handler_errors = logging.StreamHandler()
error_filter = SoloErroresFilter()
console_handler_errors.addFilter(error_filter)
logger.addHandler(console_handler_errors)

# Handler para un archivo (mostrar todos los logs)
file_handler_all = logging.FileHandler('modulo.log')
logger.addHandler(file_handler_all)

# Emitir logs
logger.debug("Información de depuración del módulo.")
logger.info("Información general del módulo.")
logger.error("¡Se produjo un error crítico en el módulo!")
logger.warning("Advertencia menor en el módulo.")
