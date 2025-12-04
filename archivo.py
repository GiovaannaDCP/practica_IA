from typing import Any, List


def buscar_elemento(lista: List[Any], elemento: Any) -> int:
    """
    Busca `elemento` en `lista` y devuelve el índice de su primera aparición.
    Si no se encuentra, devuelve -1.

    Implementación usando un bucle while para recorrer la lista de forma
    eficiente evitando búsquedas adicionales o llamadas repetidas a métodos.
    Complejidad: O(n) en el peor caso.

    Ejemplos:
    >>> buscar_elemento([3, 5, 2], 5)
    1
    >>> buscar_elemento(['a', 'b', 'c'], 'x')
    -1
    """
    if lista is None:
        return -1

    i = 0
    n = len(lista)
    # almacenar la lista en una variable local no es necesario aquí porque
    # `lista` ya es local, pero mantenemos `n` precalculado para evitar
    # llamadas repetidas a len() en el bucle.
    while i < n:
        if lista[i] == elemento:
            return i
        i += 1
    return -1


def buscar_elemento_rapido(lista: List[Any], elemento: Any) -> int:
    """
    Versión alternativa que usa el método de lista .index(), que está
    implementado en C y suele ser más rápido que un bucle en Python puro.
    Devuelve -1 si no se encuentra.
    """
    if lista is None:
        return -1
    try:
        return lista.index(elemento)
    except ValueError:
        return -1


if __name__ == "__main__":
    # Ejemplos de uso rápido
    print(buscar_elemento([1, 2, 3, 4], 3))   # salida esperada: 2
    print(buscar_elemento(["x", "y", "z"], "a"))  # salida esperada: -1
    print(buscar_elemento_rapido([1, 2, 3, 4], 3))   # salida esperada: 2
    print(buscar_elemento_rapido(["x", "y", "z"], "a"))  # salida esperada: -1
