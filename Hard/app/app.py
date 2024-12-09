from flask import Flask, request, jsonify, render_template
import MySQLdb
import json
import os

app = Flask(__name__)

# Configurații pentru baza de date
DB_HOST = "db"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "procesare_db"

def init_db():
    """Initialize the database by running the init.sql script."""
    try:
        # Conectare la serverul MySQL
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)
        cursor = db.cursor()

        # Citirea fișierului init.sql
        script_path = os.path.join(os.path.dirname(__file__), 'db', 'init.sql')
        with open(script_path, 'r') as file:
            init_sql = file.read()

        # Executarea scriptului SQL
        cursor.execute(init_sql)

        # Confirmarea
        db.commit()

        # Verificare dacă baza de date și tabelul există
        cursor.execute("SHOW TABLES LIKE 'processed_data'")
        result = cursor.fetchone()

        if result:
            print("Tabela 'processed_data' există.")
        else:
            print("Tabela 'processed_data' nu a fost găsită.")

        # Închide conexiunea
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Eroare la conectarea sau interacționarea cu baza de date: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form['data']
    if not data:
        return "Vă rugăm să introduceți date valide!"
    
    # Exemplu de procesare
    processed_data = {
        "original": data,
        "length": len(data),
        "reversed": data[::-1],
        "uppercased": data.upper(),
        "words": data.split()
    }

    # Conectare la baza de date MySQL folosind mysqlclient
    try:
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
        cursor = db.cursor()

        # Inserarea datelor procesate în baza de date
        query = """
            INSERT INTO processed_data (original, length, reversed, uppercased, words)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data, len(data), data[::-1], data.upper(), json.dumps(data.split())))

        # Confirmarea inserării
        db.commit()

        # Închide conexiunea
        cursor.close()
        db.close()
        
        return jsonify(processed_data)

    except MySQLdb.Error as e:
        return f"Eroare la conectarea sau interacționarea cu baza de date: {e}"

if __name__ == '__main__':
    # Inițializarea bazei de date înainte de a porni aplicația
    init_db()
    app.run(host='0.0.0.0', port=5000)
