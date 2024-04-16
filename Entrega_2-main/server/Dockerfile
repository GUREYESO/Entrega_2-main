FROM python:3.9
 
# Establece el directorio de trabajo en /app

WORKDIR /app
 
# Copia el archivo requirements.txt al directorio de trabajo
# Instala las dependencias

RUN pip install mysql 
RUN pip install mysql-connector-python

# Copia el resto del código al directorio de trabajo

COPY . .
 
# Ejecuta el servidor cuando se inicie el contenedor

CMD ["python", "server.py"]
