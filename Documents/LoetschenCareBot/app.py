from flask import Flask, request, jsonify, render_template
import pyodbc

app = Flask(__name__)

# Startseite
@app.route('/')
def home():
    return "LoetschenCareBot läuft erfolgreich!"

# Bot Route, um Fragen zu stellen
@app.route('/bot', methods=['POST'])
def bot():
    data = request.get_json()
    question = data.get('question')

    # Debug-Ausgabe
    print(f"Empfangene Frage: {question}")

    # Verbindung zur SQL-Datenbank herstellen
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=loetschental-sql-server.database.windows.net;'
        'DATABASE=loetschental_care_data;'
        'UID=loetschental_admin;'
        'PWD=Hockenhorn3923*'
    )
    cursor = conn.cursor()

    # Debug-Ausgabe
    print("Datenbankverbindung erfolgreich")

    try:
        # Verwende LIKE, um nach ähnlichen Fragen zu suchen
        cursor.execute("SELECT column3 FROM CareHome_Medizinische_Versorgung_ExpertQA_Interviews WHERE column2 LIKE ?", '%' + question + '%')
        result = cursor.fetchone()
        if result:
            print(f"Gefundene Antwort: {result[0]}")
            return jsonify({"answer": result[0]})
        else:
            print("Keine Antwort gefunden")
            return jsonify({"answer": 'Leider konnte ich keine Antwort auf diese Frage finden.'})
    except Exception as e:
        print(f"Fehler bei der Abfrage: {e}")
        return jsonify({"answer": 'Fehler bei der Abfrage'})

# Route, um die ask_bot.html Seite anzuzeigen
@app.route('/ask-bot')
def ask_bot():
    return render_template('ask_bot.html')

if __name__ == '__main__':
    app.run(debug=True)