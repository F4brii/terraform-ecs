# Usa la última versión estable de Python (3.12)
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de la aplicación
COPY main.py .

# Instalar dependencias necesarias
RUN pip install --no-cache-dir fastapi uvicorn[standard] kafka-python pydantic

# Exponer el puerto por el que escuchará Uvicorn
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
