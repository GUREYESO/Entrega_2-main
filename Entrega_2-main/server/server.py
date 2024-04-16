import socket
import mysql.connector
import pickle

# Conectarse a la base de datos MySQL
db_connection = mysql.connector.connect(
    host="mysql",
    user="root",
    password="gus",
    database="Entrega_2"
)

# Creamos el cursor para ejecutar consultas SQL
cursor = db_connection.cursor()

# Creamos el socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenemos el nombre del host y el número de puerto
host = socket.gethostname()
port = 12345

# Ligamos el socket al host y el puerto
server_socket.bind((host, port))

# Escuchamos conexiones entrantes
server_socket.listen(5)

print(f"Servidor escuchando en {host}:{port}")

while True:
    # Esperamos por una conexión
    client_socket, addr = server_socket.accept()

    print(f"Conexión establecida desde {addr}")

    # Recibimos el número de teléfono del cliente
    data = client_socket.recv(1024)
    telefono = int(data.decode())

    # Consultamos la base de datos para obtener la información de la persona
    query = f"SELECT * FROM personas WHERE dir_tel = {telefono}"
    cursor.execute(query)
    persona_info = cursor.fetchone()

    # Enviamos la información de la persona de vuelta al cliente
    if persona_info:
        response = pickle.dumps(persona_info)  # Convertimos la información a bytes
    else:
        response = pickle.dumps("Persona no encontrada")
    client_socket.send(response)

    # Cerramos la conexión con el cliente
    client_socket.close()
