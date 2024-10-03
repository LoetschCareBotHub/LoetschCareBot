import requests

api_key = "f467f99a2636411a9f28503db580cef2"
endpoint = "https://loetschentalcareai.cognitiveservices.azure.com/text/analytics/v3.0/sentiment"

headers = {
    'Ocp-Apim-Subscription-Key': api_key,
    'Content-Type': 'application/json'
}

data = {
    'documents': [
        {'id': '1', 'language': 'en', 'text': 'Hello, world!'}
    ]
}

response = requests.post(endpoint, headers=headers, json=data)
print(response.json())

import pyodbc

# Funktion, um alle Tabellen abzufragen
def datenbank_abfragen_alle_tabellen():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=loetschental-sql-server.database.windows.net;'  # Dein Servername
        'DATABASE=loetschental_care_data;'  # Dein Datenbankname
        'UID=loetschental_admin;'  # Dein Benutzername
        'PWD=Hockenhorn3923*'  # Dein Passwort
    )
    
    cursor = conn.cursor()

    # Abrufen aller Tabellen aus der Datenbank
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_TYPE='BASE TABLE';")
    tabellen = cursor.fetchall()

    # Schleife durch alle Tabellen und zeige nur nicht-leere Werte an
    for tabelle in tabellen:
        print(f"Daten aus Tabelle: {tabelle.TABLE_NAME}")
        query = f"SELECT * FROM {tabelle.TABLE_NAME};"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Zeige die Daten an, aber nur wenn nicht-leere Werte vorhanden sind
        for row in rows:
            if any(row):  # Nur nicht-leere Zeilen ausgeben
                print([value for value in row if value is not None])
    
    # Verbindung schließen
    cursor.close()
    conn.close()

# Funktion aufrufen, um alle Tabellen abzufragen und die Ausgabe anzupassen
datenbank_abfragen_alle_tabellen()

