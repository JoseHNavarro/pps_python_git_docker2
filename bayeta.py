def frotar(n_frases: int = 1) -> list:
    """
    Devuelve una lista con N frases (siempre la misma frase repetida).
    Args:
        n_frases (int): Número de frases a incluir en la lista.
    Returns:
        list: Lista con N frases.
    """
    frase_repetida = "Esta es la misma frase, pero repetida."
    lista_frases = [frase_repetida] * n_frases
    return lista_frases

# Ejemplo de uso:
if __name__ == "__main__":
    resultado = frotar(n_frases=5)
    print(resultado)

