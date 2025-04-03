FROM python:3.13

# Directorio de trabajo
WORKDIR /app

# Se copia el script de Python 
COPY sim.py /app/

# Ejecutar en el contenedor el script
CMD ["python", "sim.py"]
