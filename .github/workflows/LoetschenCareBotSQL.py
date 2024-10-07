import pyodbc

# Verbindung zur SQL-Datenbank herstellen
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=loetschental-sql-server.database.windows.net;'
    'DATABASE=loetschental_care_data;'
    'UID=loetschental_admin;'
    'PWD=Hockenhorn3923*'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM CareHome_Medizinische_Versorgung_ExpertQA_Interviews")
rows = cursor.fetchall()

# Ausgabe der SQL-Ergebnisse
for row in rows:
    print(row)