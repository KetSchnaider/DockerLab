from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Procesare de date</h1>
        <form action="/process" method="post">
            <textarea name="data" placeholder="Introduceți datele aici" rows="5" cols="40"></textarea><br>
            <input type="submit" value="Procesează">
        </form>
    '''

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
    
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
