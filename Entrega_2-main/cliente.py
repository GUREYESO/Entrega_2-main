import socket
import pickle

# Creamos el socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenemos el nombre del host y el número de puerto del servidor
host = socket.gethostname()  # Cambia esto por la dirección IP del servidor si es necesario
port = 12345

# Nos conectamos al servidor
client_socket.connect((host, port))

# Solicitamos al usuario que ingrese el número de teléfono a buscar
telefono = input("Ingrese el número de teléfono a buscar: ")

# Enviamos el número de teléfono al servidor
client_socket.send(telefono.encode())

# Recibimos la respuesta del servidor
response = client_socket.recv(1024)

# Procesamos la respuesta (convertimos de bytes a objeto Python)
respuesta_objeto = pickle.loads(response)

# Mostramos la respuesta al usuario
print(respuesta_objeto)

# Cerramos la conexión con el servidor
client_socket.close()
