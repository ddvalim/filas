class Queue:
    def __init__(self, limite):
        self.__fila = []
        self.__limite = limite

    def is_empty(self):
        if len(self.__fila) == 0:
            print("A fila está vazia!")
            return
        else:
            print("A fila não está vazia!")
            return
    
    def is_full(self):
        if len(self.__fila) == self.__limite:
            print("A fila está cheia!")
            return
        else:
            print("A fila não está cheia!")
            return

    def show_queue(self):
        print(self.__fila)
    
    def push(self, elemento:int):
        if len(self.__fila) < self.__limite:
            return self.__fila.append(elemento)
        else:
            raise Exception("Erro: a fila está cheia!")
    
    def pop(self):
        if len(self.__fila) != 0:
            self.__fila.pop(0)
        else:
            raise Exception("Erro: a fila está vazia!")


queue = Queue(10)
queue.push(2)
queue.push(5)
queue.push(8)
queue.push(7)
queue.show_queue()
queue.pop()
queue.show_queue()
queue.pop()
queue.show_queue()
