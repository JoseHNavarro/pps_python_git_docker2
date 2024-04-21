import random
from mongo import instanciar, consultar

def frotar(n_frases):
    cliente_mongo, frases_auspiciosas = instanciar()

    
    frases = []
    docs = consultar(n_frases, frases_auspiciosas)  # Obtenemos los documentos con frases auspiciosas de la base de datos
    for doc in docs:
        frase = doc["frase"]
        frases.append(frase)
    respuesta = []
    for i in range(n_frases):
        frase = random.choice(frases)
        respuesta.append(frase)

    
    cliente_mongo.close()

    return respuesta  # Devolvemos la respuesta
