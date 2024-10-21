def new_node(key, value):
    """Estructura que contiene la información a guardar en un nodo de un árbol binario

    Se crea un nodo con los siguientes atributos:
    - **key**: Llave del nodo
    - **value**: Valor del nodo
    - **size**: Tamaño del nodo. Inicializado en 1
    - **left**: Hijo izquierdo del nodo. Inicializado en ``None``
    - **right**: Hijo derecho del nodo. Inicializado en ``None``
    - **type**: Tipo de árbol. Inicializado en "BST"

    :param key: Llave del nodo
    :type key: any
    :param value: Valor del nodo
    :type value: any

    :returns: Nodo creado
    :rtype: bst_node
    """
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "type": "BST",
    }
    return node


def get_value(my_node):
    """Retorna el valor asociado a un nodo

    :param my_node: El nodo con la iformación
    :type my_node: bst_node

    :returns: El valor almacenado en el nodo
    :rtype: any
    """
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value


def get_key(my_node):
    """Retorna la llave asociada a un nodo

    :param my_node: El nodo con la información
    :type my_node: bst_node

    :returns: La llave almacenada en el nodo
    :rtype: any
    """
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key



def new_map():
    my_bst={
        "root": None,
        "type": "BST"
        }
    return my_bst

def put(my_bst, key, value):
    """Inserta o reemplaza una pareja llave-valor en el BST."""
    
    def insert_node(node, key, value):
        # Si el nodo es None, crear un nuevo nodo
        if node is None:
            return new_node(key, value)
        
        # Comparar las llaves para decidir dónde insertar
        if key < node["key"]:
            node["left"] = insert_node(node["left"], key, value)
        elif key > node["key"]:
            node["right"] = insert_node(node["right"], key, value)
        else:
            node["value"] = value  # Reemplazar el valor si la llave ya existe

        # Actualizar el tamaño del nodo
        node["size"] = 1 + (node["left"]["size"] if node["left"] else 0) + (node["right"]["size"] if node["right"] else 0)
        
        return node
    
    # Insertar en el árbol a partir de la raíz
    my_bst["root"] = insert_node(my_bst["root"], key, value)

def size(my_bst):
    """Devuelve el tamaño del subárbol.
    
    :param node: El nodo raíz del subárbol
    :return: Tamaño del subárbol
    """
    root = my_bst["root"]
    if root is None:
        return 0
    return root["size"]  # Retorna el tamaño del nodo raíz

def get(my_bst, key):
    root = my_bst["root"]
    
    # Función auxiliar para buscar el nodo en el árbol binario de búsqueda
    def _get_node(node, key):
        if node is None:
            return None
        node_key = get_key(node)  # Obtén la llave del nodo actual
        if key == node_key:
            return node
        elif key < node_key:
            return _get_node(node["left"], key)  # Recurre al hijo izquierdo
        else:
            return _get_node(node["right"], key)  # Recurre al hijo derecho

    result_node = _get_node(root, key)  # Busca el nodo correspondiente a la llave

    if result_node is not None:
        return get_value(result_node)  # Retorna el valor del nodo encontrado
    else:
        return None  # Si no se encuentra la llave, retorna None

 
def remove(my_bst, key):
    root = my_bst["root"]

    if root is None:
        return None  # Si el árbol está vacío, no hay nada que eliminar

    # Función auxiliar para encontrar el nodo con la llave mínima en un subárbol
    def encontrar_min(node):
        while node["left"] is not None:
            node = node["left"]
        return node

    # Función auxiliar para actualizar el tamaño de un nodo
    def update_size(node):
        if node is None:
            return 0
        left_size = node["left"]["size"] if node["left"] else 0
        right_size = node["right"]["size"] if node["right"] else 0
        node["size"] = 1 + left_size + right_size
        return node["size"]

    # Función auxiliar para eliminar el nodo recursivamente
    def _remove(node, key):
        if node is None:
            return None

        node_key = get_key(node)

        if key < node_key:
            node["left"] = _remove(node["left"], key)  # Eliminar del subárbol izquierdo
        elif key > node_key:
            node["right"] = _remove(node["right"], key)  # Eliminar del subárbol derecho
        else:
            # Caso 1: Nodo sin hijos
            if node["left"] is None and node["right"] is None:
                return None  # Elimina el nodo

            # Caso 2: Nodo con un solo hijo
            elif node["left"] is None:
                return node["right"]
            elif node["right"] is None:
                return node["left"]

            # Caso 3: Nodo con dos hijos
            else:
                # Encuentra el sucesor (nodo con el valor mínimo en el subárbol derecho)
                successor = encontrar_min(node["right"])
                node["key"] = get_key(successor)
                node["value"] = get_value(successor)
                # Elimina el sucesor del subárbol derecho
                node["right"] = _remove(node["right"], get_key(successor))

        # Actualiza el tamaño del nodo actual después de la eliminación
        update_size(node)
        return node

    # Llama a la función auxiliar para eliminar el nodo y actualizar el árbol
    my_bst["root"] = _remove(root, key)

    return my_bst  # Devuelve el árbol con el nodo eliminado

    

def contains(my_bst, key):
    root = my_bst["root"]

    # Función auxiliar recursiva para buscar la llave en el árbol
    def _contains(node, key):
        if node is None:
            return False  # Si el nodo es None, la llave no está en el árbol
        
        node_key = get_key(node)  # Obtiene la llave del nodo actual
        
        if key == node_key:
            return True  # Si la llave coincide, la encontramos
        elif key < node_key:
            return _contains(node["left"], key)  # Buscar en el subárbol izquierdo
        else:
            return _contains(node["right"], key)  # Buscar en el subárbol derecho

    # Llamada a la función auxiliar empezando desde la raíz
    return _contains(root, key)

def is_empty(my_bst):
    
    return my_bst["root"] is None
    

def key_set(my_bst):
    root = my_bst["root"]
    keys = []

    # Función para hacer un recorrido en orden y recoger las llaves
    def _in_order(node):
        if node is not None:
            _in_order(node["left"])  # Visita el hijo izquierdo
            keys.append(node["key"])  # Guarda la llave
            _in_order(node["right"])  # Visita el hijo derecho

    _in_order(root)  # Llama a la función auxiliar

    return {
        "size": len(keys),     # Devuelve el tamaño de las llaves
        "elements": keys       # Devuelve la lista de llaves
    }

            

def value_set(my_bst):
    # Función auxiliar para recorrer el árbol y recolectar los valores
    def _collect_values(node, values):
        if node is None:
            return
        # Recorrido en orden para recolectar los valores
        _collect_values(node["left"], values)
        values.append(node["value"])
        _collect_values(node["right"], values)

    root = my_bst.get("root", None)
    values = []
    
    # Recolectar los valores empezando desde la raíz
    _collect_values(root, values)
    
    # Retornar la estructura esperada
    return {
        "size": len(values),  # Tamaño de la lista de valores
        "elements": values    # Lista con todos los valores
    }



def min_key(my_bst):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)

    # Si el árbol está vacío, retornar None
    if root is None:
        return None

    # Recorrer el árbol hacia la izquierda para encontrar el menor nodo
    current_node = root
    while current_node["left"] is not None:
        current_node = current_node["left"]

    # Retornar la llave del nodo más a la izquierda (el menor)
    return current_node["key"]


def max_key(my_bst):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)

    # Si el árbol está vacío, retornar None
    if root is None:
        return None
    
    # Recorrer el árbol hacia la derecha para encontrar el menor nodo
    actual_node = root
    while actual_node["right"] is not None:
        actual_node = actual_node["right"]
    # Retornar la llave del nodo más a la derecha (el mayor)
    return actual_node["key"]    

   
def delete_min(my_bst):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)

    # Si el árbol está vacío, retornar el árbol tal cual
    if root is None:
        return my_bst

    # Función auxiliar para encontrar y eliminar el nodo más pequeño
    def _delete_min_node(node):
        # Si el nodo actual no tiene hijo izquierdo, hemos encontrado el menor
        if node["left"] is None:
            return node["right"]  # Eliminar el nodo y retornar su hijo derecho (puede ser None)
        
        # Continuar buscando por el hijo izquierdo
        node["left"] = _delete_min_node(node["left"])

        # Actualizar el tamaño del nodo después de eliminar el menor
        node["size"] = 1 + (node["left"]["size"] if node["left"] else 0) + (node["right"]["size"] if node["right"] else 0)

        return node

    # Reemplazar la raíz con el nuevo árbol después de eliminar el nodo mínimo
    my_bst["root"] = _delete_min_node(root)
    
    return my_bst


def delete_max(my_bst):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)

    # Si el árbol está vacío, retornar el árbol tal cual
    if root is None:
        return my_bst

    # Función auxiliar para encontrar y eliminar el nodo más grande
    def _delete_max_node(node):
        # Si el nodo actual no tiene hijo derecho, hemos encontrado el mayor
        if node["right"] is None:
            return node["left"]  # Eliminar el nodo y retornar su hijo izquierdo (puede ser None)

        # Continuar buscando por el hijo derecho
        node["right"] = _delete_max_node(node["right"])

        # Actualizar el tamaño del nodo después de eliminar el mayor
        node["size"] = 1 + (node["left"]["size"] if node["left"] else 0) + (node["right"]["size"] if node["right"] else 0)

        return node

    # Reemplazar la raíz con el nuevo árbol después de eliminar el nodo máximo
    my_bst["root"] = _delete_max_node(root)
    
    return my_bst


def floor(my_bst, key):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)
    
    # Función auxiliar para encontrar la clave más grande menor o igual a la clave dada
    def _floor(node, key):
        if node is None:
            return None
        
        node_key = node["key"]

        if key == node_key:
            return node_key  # Si la llave es exactamente igual a la clave, retornarla

        if key < node_key:
            # Si la llave buscada es menor que la clave del nodo, buscar en el subárbol izquierdo
            return _floor(node["left"], key)

        # Si la llave buscada es mayor que la clave del nodo, buscar en el subárbol derecho
        # y comparar el resultado con la clave actual
        right_result = _floor(node["right"], key)
        if right_result is not None:
            return right_result
        else:
            return node_key  # Si no hay mejor resultado en el subárbol derecho, retornar la clave actual

    # Llamar a la función auxiliar y retornar el resultado
    return _floor(root, key)


def ceiling(my_bst, key):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)
    
    # Función auxiliar para encontrar la clave más pequeña mayor o igual a la clave dada
    def _ceiling(node, key):
        if node is None:
            return None
        
        node_key = node["key"]

        if key == node_key:
            return node_key  # Si la llave es exactamente igual a la clave, retornarla

        if key > node_key:
            # Si la llave buscada es mayor que la clave del nodo, buscar en el subárbol derecho
            return _ceiling(node["right"], key)

        # Si la llave buscada es menor que la clave del nodo, buscar en el subárbol izquierdo
        # y comparar el resultado con la clave actual
        left_result = _ceiling(node["left"], key)
        if left_result is not None:
            return left_result  # Si encontramos una clave en el subárbol izquierdo que es mayor o igual, retornarla
        else:
            return node_key  # Si no hay mejor resultado en el subárbol izquierdo, retornar la clave actual

    # Llamar a la función auxiliar y retornar el resultado
    return _ceiling(root, key)

def select(my_bst, pos):
    # Empezar desde la raíz del árbol
    root = my_bst.get("root", None)
    
    # Función auxiliar para contar el tamaño del subárbol
    def _size(node):
        if node is None:
            return 0
        return node.get("size", 1)  # Retorna el tamaño del nodo, por defecto es 1

    # Función auxiliar para encontrar la k-ésima llave más pequeña
    def _select(node, pos):
        if node is None:
            return None

        left_size = _size(node["left"])  # Tamaño del subárbol izquierdo

        if pos < left_size:
            # Si la posición es menor que el tamaño del subárbol izquierdo, buscar en el subárbol izquierdo
            return _select(node["left"], pos)
        elif pos > left_size:
            # Si la posición es mayor, buscar en el subárbol derecho
            return _select(node["right"], pos - left_size - 1)
        else:
            # Si la posición es igual, hemos encontrado la k-ésima llave más pequeña
            return node["key"]

    # Llamar a la función auxiliar y retornar el resultado
    return _select(root, pos)


def rank(my_bst, key):
    root = my_bst.get("root", None)

    # Función auxiliar para contar el tamaño del subárbol
    def _size(node):
        if node is None:
            return 0
        return node.get("size", 1)  # Retorna el tamaño del nodo, por defecto es 1

    # Función auxiliar para calcular el rango
    def _rank(node, key):
        if node is None:
            return 0

        node_key = node["key"]

        if key < node_key:
            # Si la llave es menor que la llave del nodo, buscar en el subárbol izquierdo
            return _rank(node["left"], key)
        elif key > node_key:
            # Si la llave es mayor, contar el tamaño del subárbol izquierdo más 1 (la llave del nodo actual) más lo que se encuentre en el subárbol derecho
            return 1 + _size(node["left"]) + _rank(node["right"], key)
        else:
            # Si son iguales, contar solo el tamaño del subárbol izquierdo
            return _size(node["left"])

    return _rank(root, key)

def height(my_bst):
    root = my_bst.get("root", None)

    # Función auxiliar para calcular la altura de un nodo
    def _height(node):
        if node is None:
            return -1  # Retorna -1 para que la altura de un árbol vacío sea 0
        else:
            left_height = _height(node["left"])   # Altura del subárbol izquierdo
            right_height = _height(node["right"]) # Altura del subárbol derecho
            return 1 + max(left_height, right_height) # La altura es 1 + la mayor altura de los subárboles

    return _height(root)

def keys(my_bst, key_lo, key_hi):
    root = my_bst.get("root", None)
    result = []  # Lista para almacenar las llaves en el rango

    # Función auxiliar para realizar el recorrido del árbol
    def _keys(node):
        if node is None:
            return
        
        # Obtiene la llave del nodo actual
        node_key = node["key"]

        # Si la llave actual es mayor que el límite inferior, recursar al subárbol izquierdo
        if node_key > key_lo:
            _keys(node["left"])
        
        # Si la llave actual está dentro del rango, añadirla a la lista de resultados
        if key_lo <= node_key <= key_hi:
            result.append(node_key)
        
        # Si la llave actual es menor que el límite superior, recursar al subárbol derecho
        if node_key < key_hi:
            _keys(node["right"])

    # Iniciar el recorrido del árbol desde la raíz
    _keys(root)
    
    return {
        "size": len(result),  # Tamaño de la lista de valores
        "elements": result    # Lista con todos los valores
        
    }

def values(my_bst, key_lo, key_hi):
    root = my_bst.get("root", None)
    result = []  # Lista para almacenar los valores en el rango

    # Función auxiliar para realizar el recorrido del árbol
    def _values(node):
        if node is None:
            return
        
        # Obtiene la llave del nodo actual
        node_key = node["key"]

        # Si la llave actual es mayor que el límite inferior, recursar al subárbol izquierdo
        if node_key > key_lo:
            _values(node["left"])
        
        # Si la llave actual está dentro del rango, añadir el valor a la lista de resultados
        if key_lo <= node_key <= key_hi:
            result.append(node["value"])
        
        # Si la llave actual es menor que el límite superior, recursar al subárbol derecho
        if node_key < key_hi:
            _values(node["right"])

    # Iniciar el recorrido del árbol desde la raíz
    _values(root)
    
    return {
        "size": len(result),  # Tamaño de la lista de valores
        "elements": result    # Lista con todos los valores
    }
