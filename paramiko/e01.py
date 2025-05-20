import paramiko

class ClienteSSH:
    def __init__(self, hostname, port, username, password=None, key_filename=None):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.client = None
        self.sftp = None

    def conectar(self):
        """Establece la conexión SSH."""
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Para entornos de prueba, considera KnownHostsPolicy
            if self.key_filename:
                self.client.connect(hostname=self.hostname, port=self.port, username=self.username, key_filename=self.key_filename)
            else:
                self.client.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            self.sftp = self.client.open_sftp()
            print(f"Conexión SSH establecida con {self.hostname}:{self.port}")
            return True
        except paramiko.AuthenticationException:
            print("Error de autenticación.")
            return False
        except paramiko.SSHException as e:
            print(f"No se pudo establecer la conexión SSH: {e}")
            return False
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False

    def existe_archivo(self, ruta_remota):
        """Verifica si un archivo existe en la ruta remota."""
        if not self.sftp:
            print("No hay una conexión SFTP activa.")
            return False
        try:
            self.sftp.stat(ruta_remota)
            print(f"El archivo '{ruta_remota}' existe en el servidor.")
            return True
        except FileNotFoundError:
            print(f"El archivo '{ruta_remota}' no existe en el servidor.")
            return False
        except Exception as e:
            print(f"Ocurrió un error al verificar el archivo: {e}")
            return False

    def cerrar_conexion(self):
        """Cierra la conexión SSH y SFTP."""
        if self.sftp:
            self.sftp.close()
            print("Conexión SFTP cerrada.")
        if self.client:
            self.client.close()
            print("Conexión SSH cerrada.")
        self.client = None
        self.sftp = None

if __name__ == "__main__":
    # Reemplaza con tus propios datos de conexión y ruta de archivo
    hostname = "tu_servidor.com"
    port = 22
    username = "tu_usuario"
    password = "tu_contraseña"  # O usa key_filename
    ruta_archivo_remoto = "/ruta/al/archivo/remoto.txt"

    ssh_client = ClienteSSH(hostname, port, username, password=password) # O key_filename="ruta/a/tu/clave_privada"

    if ssh_client.conectar():
        ssh_client.existe_archivo(ruta_archivo_remoto)
        ssh_client.cerrar_conexion()
