from conection.conection import Conection

class ModelProductos:
    def __init__(self):
        self.model=Conection('productos')

    def get_all_productos(self, colum_order):
        return self.model.get_all(colum_order)
         
    def insert_productos(self, data):
        return self.model.insert(data)

    def update_productos(self, values_to_update, conditions_filter):
        return self.model.update(values_to_update, conditions_filter)

    def delete_producto(self,conditions_filter):
        return self.model.delete(conditions_filter)