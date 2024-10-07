import requests
import pymssql

# API-Schlüssel und Endpunkt für die Sentiment-Analyse
api_key = "f467f99a2636411a9f28503db580cef2"
endpoint = "https://loetschentalcareai.cognitiveservices.azure.com/text/analytics/v3.0/sentiment"

# Header für die API-Anfrage
headers = {
    'Ocp-Apim-Subscription-Key': api_key,
    'Content-Type': 'application/json'
}

# Daten für die Sentiment-Analyse
data = {
    'documents': [
        {'id': '1', 'language': 'en', 'text': 'Hello, world!'}
    ]
}

# Senden der Anfrage an die Sentiment-Analyse-API
response = requests.post(endpoint, headers=headers, json=data)
print(response.json())

# Funktion, um alle Tabellen aus der Datenbank abzufragen
def datenbank_abfragen_alle_tabellen():
    # Verbindung zur SQL-Datenbank mit pymssql herstellen
    conn = pymssql.connect(
        server='loetschental-sql-server.database.windows.net',  # Dein Servername
        user='loetschental_admin',  # Dein Benutzername
        password='Hockenhorn3923*',  # Dein Passwort
        database='loetschental_care_data'  # Dein Datenbankname
    )

    cursor = conn.cursor()

    # Abrufen aller Tabellen aus der Datenbank
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_TYPE='BASE TABLE';")
    tabellen = cursor.fetchall()

    # Schleife durch alle Tabellen und zeige nur nicht-leere Werte an
    for tabelle in tabellen:
        print(f"Daten aus Tabelle: {tabelle[0]}")
        query = f"SELECT * FROM {tabelle[0]};"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Zeige die Daten an, aber nur wenn nicht-leere Werte vorhanden sind
        for row in rows:
            if any(row):  # Nur nicht-leere Zeilen ausgeben
                print([value for value in row if value is not None])

    # Verbindung schließen
    cursor.close()
    conn.close()

# Funktion aufrufen, um alle Tabellen abzufragen
datenbank_abfragen_alle_tabellen()