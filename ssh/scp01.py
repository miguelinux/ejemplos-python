#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
import paramiko
import scp
import os

def copiar_archivo_ssh(hostname, port, username, password, ruta_local, ruta_remota):
    """
    Copia un archivo de la computadora local a una computadora remota usando SSH.

    Args:
        hostname (str): La dirección IP o nombre de host de la computadora remota.
        port (int): El puerto SSH de la computadora remota (normalmente 22).
        username (str): El nombre de usuario para la conexión SSH.
        password (str): La contraseña para la conexión SSH.
        ruta_local (str): La ruta completa del archivo en la computadora local.
        ruta_remota (str): La ruta completa donde se guardará el archivo en la computadora remota.

    Returns:
        bool: True si la copia fue exitosa, False en caso contrario.
    """
    try:
        # Crear un objeto cliente SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Para agregar automáticamente la clave del host si no está en known_hosts

        # Conectar al servidor remoto
        client.connect(hostname=hostname, port=port, username=username, password=password)

        # Usar el cliente SCP para la transferencia de archivos
        with scp.SCPClient(client.get_transport()) as scp_client:
            scp_client.put(ruta_local, ruta_remota)

        print(f"Archivo '{ruta_local}' copiado exitosamente a '{hostname}:{ruta_remota}'")
        return True

    except paramiko.AuthenticationException:
        print("Error de autenticación: Credenciales incorrectas.")
        return False
    except paramiko.SSHException as e:
        print(f"Error de conexión SSH: {e}")
        return False
    except FileNotFoundError:
        print(f"Error: El archivo local '{ruta_local}' no fue encontrado.")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return False
    finally:
        if 'client' in locals() and client.get_transport().is_active():
            client.close()

if __name__ == "__main__":
    # --- CONFIGURACIÓN ---
    hostname_remoto = "tu_direccion_ip_o_hostname"  # Reemplaza con la IP o hostname de la computadora remota
    puerto_ssh = 22
    usuario_remoto = "tu_usuario_remoto"      # Reemplaza con tu nombre de usuario en la computadora remota
    contrasena_remota = "tu_contrasena_remota"  # Reemplaza con tu contraseña en la computadora remota
    archivo_local = "/ruta/a/tu/archivo_local.txt"  # Reemplaza con la ruta completa del archivo local que quieres copiar
    destino_remoto = "/ruta/en/la/remota/archivo_copiado.txt" # Reemplaza con la ruta donde quieres guardar el archivo en la remota

    # --- EJECUCIÓN ---
    exito = copiar_archivo_ssh(hostname_remoto, puerto_ssh, usuario_remoto, contrasena_remota, archivo_local, destino_remoto)

    if exito:
        print("La copia del archivo se completó con éxito.")
    else:
        print("La copia del archivo falló.")
