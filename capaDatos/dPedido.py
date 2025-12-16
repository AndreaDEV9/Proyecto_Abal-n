from conexion import ConexionDB

class DPedido:
    def __init__(self):
        self.__db = ConexionDB().conexionSupaBase()
        self.__tablaPedido = 'pedidos'

    def mostrarPedidos(self):
        return self.__db.table(self.__tablaPedido).select('*').execute()
    
    def insertarPedido(self, pedido : dict):
        return self.__db.table(self.__tablaPedido).insert(pedido).execute()