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
    frases_elegidas = random.sample(FRASES, n_frases)
    return frases_elegidas

# Ejemplo de uso:
if __name__ == "__main__":
    resultado = frotar(n_frases=5)
    print(resultado)

