from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola, mundo'

@app.route('/frotar/<int:n_frases>')
def frotar_bayeta(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases) # Devolvemos la lista de frases convertida en JSON como respuesta

""" if __name__ == '__main__': # Comprobamos si el fichero se ejecuta como programa principal
    app.run(debug=True, port=5000)
 """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
