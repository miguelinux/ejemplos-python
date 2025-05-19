import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO)

# Crear un logger específico
logger_db = logging.getLogger('database')
logger_api = logging.getLogger('api.users')
logger_auth = logging.getLogger('api.auth')

# Crear un handler (por ejemplo, para la consola)
console_handler = logging.StreamHandler()

# Crear un filtro que solo permita logs del logger 'database' y sus hijos
db_filter = logging.Filter('database')
console_handler.addFilter(db_filter)

# Agregar el handler al logger raíz (o a loggers específicos si lo deseas)
logging.getLogger().addHandler(console_handler)

# Emitir algunos logs
logger_db.info("Conexión a la base de datos establecida.")
logger_api.warning("Intento de acceso no autorizado.")
logger_auth.info("Usuario autenticado.")
logging.info("Información general del sistema.")
