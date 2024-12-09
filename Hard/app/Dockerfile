# Alegem imaginea de bază Python
FROM python:3.9-slim

# Instalam dependințele necesare pentru a construi mysqlclient
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    g++ \
    make

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele necesare în container
COPY . /app

# Instalăm dependențele din requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expunem portul pe care va rula aplicația Flask
EXPOSE 5000

# Comanda pentru a porni aplicația Flask
CMD ["python", "app.py"]
