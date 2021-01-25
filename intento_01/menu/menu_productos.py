from controller.productos import ProductoController
class MenuProductos:
    def __init__(self):
        self.productos=ProductoController()
        
    def menu_productos(self):
        while True:
            print('''
                Menú Productos
                1) Listar todos los productos
                2) Agregar producto
                4) Editar producto
                5) Eliminar producto
                6) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.productos.list_productos()
            elif opcion == '2':
                self.productos.insert_productos()
            elif opcion == '3':
                self.productos.update_alumno()
            elif opcion == '4':
                self.productos.delete_alumno()
            elif opcion == '5':
                break
            else:
                print('No escogiste una opción valida')
