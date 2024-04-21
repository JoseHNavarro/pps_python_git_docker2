from pymongo import MongoClient

def instanciar():
    
    cliente_mongo = MongoClient('mongodb://mongo:27017/')
    
    bd = cliente_mongo['bayeta']
    
    frases_auspiciosas = bd['frases_auspiciosas']
    
    return cliente_mongo, frases_auspiciosas

def inicializar(datos, frases_auspiciosas):
    if frases_auspiciosas.count_documents({}) == 0:
        frases_auspiciosas.insert_many(datos)

def consultar(n_frases, frases_auspiciosas):
    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))
    
    if not frases_aleatorias:
        print("No se encontraron frases auspiciosas.")
        return []
    
    for frase in frases_aleatorias:
        print(frase['frase'])
    return frases_aleatorias

def cerrar_conexion(cliente_mongo):
    # Cerrar cliente de MongoDB
    cliente_mongo.close()

if __name__ == "__main__":
    datos = [
        {"frase": "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad"},
        # ... Otras frases ...
    ]

    # Instanciar
    cliente_mongo, frases_auspiciosas = instanciar()

    inicializar(datos, frases_auspiciosas)

    # Consultar
    n_frases = 3
    consultar(n_frases, frases_auspiciosas)

    # Cerrar conexión
    cerrar_conexion(cliente_mongo)
