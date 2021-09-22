class Node:
    def __init__(self):
        self.value = 0
        self.next = None

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_on_row(self , fila , value):
        novo = Node()
        novo.value = value
        novo.next = None
        if fila.head == None:
            fila.head = novo

        else:
            fila.tail.next = novo

        fila.tail = novo

    def delet(self , fila):
        if fila.head != None:
            apagar = Node()
            apagar = fila.head
            fila.head = apagar.next
            apagar = None
            if fila.head == None:
                fila.tail = None

    def print_row(self , fila):
        auxiliar = Node()
        auxiliar = fila.head
        while auxiliar != None:
            print(auxiliar.value)
            auxiliar = auxiliar.next
