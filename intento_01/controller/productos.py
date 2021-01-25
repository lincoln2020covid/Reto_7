  
from models.productos import ModelProductos
from Otros.validar import Validacion

class ProductoController:
    def __init__(self):
        self.producto=ModelProductos()
        self.validacion_class=Validacion() #############AQUI ATENTO - PORQUE NECESITAS VALIDAR###############

    def list_productos(self):
        productos=self.producto.get_all_productos('nombre_productos')
        texto=''
        for productos in productos:
            texto+=f'''{productos}\n'''
        print (texto)

    def insert_productos(self):
        while(True):
            try:
                while(True): 
                    id_producto = int(input('Ingresa el ID del Alumno : '))
                    if(self.validacion_class.validar_id_producto(id_producto)):
                        return id_producto
                    else:
                        print('ID ingresado no existe')
                break
            except ValueError:
                print('Error: ID ingresado invalido')
        
        nombre_productos = Validacion.validar_texto('Ingrese el nombre del producto')
        stock_productos = Validacion.validar_stock('Ingresar stock del producto')
        precio_producto = Validacion.validar_precio('Ingresar el precio del producto')
        
        data={
            'id_producto':id_productos,
            'nombre_productos':nombre_productos,
            'stock_productos':stock_productos,
            'precio_producto':precio_producto
        }
        self.producto.insert_productos(data)
        print('Se creo con exito')  

