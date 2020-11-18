import pdb

class MyList:
    _head = None
    _size = 0

    def __init__(self, tupla):
        # Por ahora crearemos esta lista a partir de tuplas.
        current = None
        for i in tupla:
            node = Node(i)
            if current is None:
                self._head = node
                current = node
            else:
                current.set_next(node)
                current = current.get_next()
            self._size += 1

    def clear(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, obj):
        tail = Node(obj)
        # pdb.set_trace()
        if self._head is None:
            self._head = tail
        else:
            current = self._head
            nex = self._head.get_next()
            while nex is not None:
                current = nex
                nex = nex.get_next()
            current.set_next(tail)
        self._size += 1

    def get(self, index):
        if index < 0 or index > self._size:
            return None
        else:
            current = self._head
            cont = 0
            while current is not None:
                if cont == index:
                    return current.get_value()
                else:
                    cont += 1
                    current = current.get_next()
            return None

    def remove(self, index):
        if index < 0 or index > self._size:
            return None
        else:
            current = self._head
            prev = None
            cont = 0
            while current is not None:
                if cont == index:
                    result = current.get_value()
                    prev.set_next(current.get_next())
                    self._size -= 1
                    return result
                else:
                    cont += 1
                    prev = current
                    current = current.get_next()
            return None

    def get_index_of(self, item):
        cont = 0
        current = self._head
        while current is not None:
            if item == current.get_value():
                return cont
            else:
                cont += 1
                current = current.get_next()
        return -1

    def exists(self, item):
        return self.get_index_of(item) != -1


class Node:
    _next = None
    _value = None

    def __init__(self, value):
        self._value = value

    def set_next(self, next_node):
        self._next = next_node

    def remove_next(self):
        self._next = None

    def set_value(self, value):
        self._value = value

    def get_next(self):
        return self._next

    def get_value(self):
        return self._value
