import pyodbc

# Starte das Skript
print("Starte das Skript...")

try:
    # Verbindung zur SQL-Datenbank herstellen
    print("Verbindung zur SQL-Datenbank wird hergestellt...")
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=loetschental-sql-server.database.windows.net;'
        'DATABASE=loetschental_care_data;'
        'UID=loetschental_admin;'
        'PWD=Hockenhorn3923*'
    )
    print("Verbindung erfolgreich hergestellt!")

    # Cursor erstellen
    cursor = conn.cursor()
    print("Cursor erstellt, führe Abfrage aus...")

    # SQL-Abfrage ausführen
    cursor.execute("SELECT * FROM CareHome_Medizinische_Versorgung_ExpertQA_Interviews")
    
    # Ergebnisse abrufen
    rows = cursor.fetchall()
    
    # Ergebnisse ausgeben
    print("SQL-Abfrage erfolgreich ausgeführt, Ergebnisse werden ausgegeben:")
    for row in rows:
        print(row)

except pyodbc.Error as ex:
    print("Fehler bei der SQL-Verbindung oder Abfrage:")
    print(ex)

finally:
    # Verbindung schließen
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("Datenbankverbindung geschlossen.")