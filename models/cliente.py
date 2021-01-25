from connection.conn import Connection


class Cliente:
    def __init__(self):
        self.model = Connection('clientes')

    def get_clientes(self, order):
        return self.model.get_all(order)

    def get_cliente(self, id_object):
        return self.model.get_by_id(id_object)

    def search_cliente(self, data):
        return self.model.get_columns(data)

    def insert_cliente(self, cliente):
        return self.model.insert(cliente)

    def update_cliente(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_cliente(self, id_object):
        return self.model.delete(id_object)
