# bayeta.py

import random

# Lista de frases (puedes agregar más frases aquí)
FRASES = [
    "Esta es la primera frase.",
    "Otra frase interesante.",
    "Una tercera frase para la lista.",
    "Las frases aleatorias son geniales.",
    "Última frase, ¡prometido!"
]

def frotar(n_frases: int = 1) -> list:
    """
    Devuelve una lista con N frases aleatorias de la lista FRASES.

    Args:
        n_frases (int): Número de frases a incluir en la lista.

    Returns:
        list: Lista con N frases aleatorias.
    """
    #frases_elegidas = random.sample(FRASES, n_frases)
    frases_elegidas = []
    i=0
    while(i<n_frases):
        num_al = random.randint(0, 4) #Número aleatorio entre 0 y 4
        frases_elegidas.append(FRASES[num_al])
        i = i+1
    return frases_elegidas
