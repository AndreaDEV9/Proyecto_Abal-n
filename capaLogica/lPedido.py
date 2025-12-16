from capaDatos.dPedido import DPedido

class LPedido:
    def __init__(self):
        self.__dPedido = DPedido()

    def mostraPedidos(self):
        resultado = self.__dPedido.mostrarPedidos()
        return resultado.data if resultado else []
    
    def insetarPedidos(self, pedido: dict):
        return self.__dPedido.insertarPedido(pedido)
    
    