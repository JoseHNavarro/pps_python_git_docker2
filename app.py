from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

@app.route('/frotar/<int:n_frases>')  # Define la ruta con un parámetro n_frases
def obtener_frases(n_frases):
    frases_generadas = frotar(n_frases)  # Llama a la función frotar con el número de frases
    return jsonify(frases=frases_generadas)  # Devuelve las frases en formato JSON

if __name__ == '__main__':
    app.run(host='127.0.0.1')

