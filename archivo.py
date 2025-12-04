from typing import Any, Callable, List, Optional


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


def buscar_objeto_por_clave(lista: List[Any], clave: str, valor: Any) -> int:
    """
    Busca en `lista` el primer objeto (por ejemplo, diccionario o cualquier
    objeto con atributos) cuya clave/atributo `clave` sea igual a `valor`.
    Devuelve el índice de la primera coincidencia o -1 si no se encuentra.

    - Si el elemento es un dict, se usa obj.get(clave).
    - Si no es dict, se intenta getattr(obj, clave, sentinel).
    - Ignora elementos donde no se puede acceder a la clave/atributo.

    Ejemplos:
    >>> lista = [{"id": 1}, {"id": 2}, {"id": 3}]
    >>> buscar_objeto_por_clave(lista, "id", 2)
    1

    >>> class X: pass
    >>> a = X(); a.name = "ana"
    >>> b = X(); b.name = "juan"
    >>> buscar_objeto_por_clave([a, b], "name", "juan")
    1
    """
    if lista is None:
        return -1

    sentinel = object()
    for i, obj in enumerate(lista):
        try:
            if isinstance(obj, dict):
                if obj.get(clave, sentinel) == valor:
                    return i
            else:
                if getattr(obj, clave, sentinel) == valor:
                    return i
        except Exception:
            # si acceder falla por cualquier razón, saltamos ese elemento
            continue
    return -1


def buscar_objetos_por_clave(lista: List[Any], clave: str, valor: Any) -> List[int]:
    """
    Busca todas las posiciones en `lista` cuyos objetos tengan clave/atributo
    `clave` igual a `valor`. Devuelve la lista de índices (puede estar vacía).

    Ejemplo:
    >>> lista = [{"id": 1}, {"id": 2}, {"id": 2}]
    >>> buscar_objetos_por_clave(lista, "id", 2)
    [1, 2]
    """
    if lista is None:
        return []

    sentinel = object()
    indices: List[int] = []
    for i, obj in enumerate(lista):
        try:
            if isinstance(obj, dict):
                if obj.get(clave, sentinel) == valor:
                    indices.append(i)
            else:
                if getattr(obj, clave, sentinel) == valor:
                    indices.append(i)
        except Exception:
            continue
    return indices


def encontrar_con_predicado(lista: List[Any], predicado: Callable[[Any], bool]) -> List[Any]:
    """
    Busca y devuelve los objetos de `lista` que cumplen `predicado`.
    Útil cuando la lógica de búsqueda no se reduce a clave==valor.

    Ejemplo:
    >>> lista = [{"id": 1}, {"id": 2}, {"id": 3}]
    >>> encontrar_con_predicado(lista, lambda o: o.get("id", 0) % 2 == 1)
    [{'id': 1}, {'id': 3}]
    """
    if lista is None:
        return []

    resultados: List[Any] = []
    for obj in lista:
        try:
            if predicado(obj):
                resultados.append(obj)
        except Exception:
            # si el predicado falla para un elemento, lo ignoramos
            continue
    return resultados


if __name__ == "__main__":
    # Ejemplos de uso rápido para listas simples
    print(buscar_elemento([1, 2, 3, 4], 3))   # salida esperada: 2
    print(buscar_elemento(["x", "y", "z"], "a"))  # salida esperada: -1
    print(buscar_elemento_rapido([1, 2, 3, 4], 3))   # salida esperada: 2
    print(buscar_elemento_rapido(["x", "y", "z"], "a"))  # salida esperada: -1

    # Ejemplos con lista de diccionarios
    lista_dic = [{"id": 1, "name": "ana"}, {"id": 2, "name": "juan"}, {"id": 3}]
    print(buscar_objeto_por_clave(lista_dic, "name", "juan"))  # salida esperada: 1
    print(buscar_objeto_por_clave(lista_dic, "id", 4))  # salida esperada: -1
    print(buscar_objetos_por_clave(lista_dic, "id", 2))  # salida esperada: [1]

    # Ejemplo con objetos con atributos
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __repr__(self):
            return f"Persona({self.nombre!r}, {self.edad!r})"

    p1 = Persona("ana", 30)
    p2 = Persona("juan", 25)
    lista_obj = [p1, p2]
    print(buscar_objeto_por_clave(lista_obj, "nombre", "juan"))  # salida esperada: 1

    # Ejemplo usando predicado
    print(encontrar_con_predicado(lista_dic, lambda o: isinstance(o, dict) and o.get("id", 0) % 2 == 1))
    # salida esperada: [{'id': 1, 'name': 'ana'}, {'id': 3}]
