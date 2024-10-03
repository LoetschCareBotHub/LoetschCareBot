# Basis-Image
FROM python:3.11-slim

# Installiere den ODBC-Treiber für SQL Server
RUN apt-get update && apt-get install -y msodbcsql17

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiere den Rest der Anwendung
COPY . .

# Führe die Python-Anwendung aus
CMD ["python", "LoetschenCareBot.py"]
