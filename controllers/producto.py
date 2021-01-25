from models.producto import Producto
from models.factura import Factura
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class ProductoController:
    def __init__(self):
        self.producto = Producto()
        self.factura = Factura()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Productos
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_productos()
                elif respuesta == 2:
                    self.search_producto()
                elif respuesta == 3:
                    self.insert_producto()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_productos(self):
        try:
            print('''
            ==========================
                Listar Productos
            ==========================
            ''')
            productos = self.producto.get_productos('id_productos')
            print(print_table(productos, ['ID', 'nombre_productos', 'stock_productos', 'precio_productos']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_producto(self):
        print('''
        ========================
            Buscar Producto
        ========================
        ''')
        try:
            id_productos = input_data("Ingrese el ID del producto >> ", "int")
            producto = self.producto.get_producto({
                'id_productos': id_productos
            })
            print(print_table(producto, ['ID', 'nombre_productos', 'stock_productos', 'precio_productos']))

            if producto:
                if question('¿Deseas dar mantenimiento al producto?'):
                    opciones = ['Asignar Factura', 'Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.assign_curso(id_productos, producto)
                    elif respuesta == 2:
                        self.update_producto(producto_id)
                    elif respuesta == 3:
                        self.delete_producto(producto_id)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_producto(self):
        nombre_productos = input_data('Ingrese el nombre del producto >> ')
        stock_productos = input_data('Ingrese el stock del producto >> ', 'int')
        precio_productos = input_data('Ingrese el precio del producto >> ')
        self.producto.insert_producto({
            'nombre_productos': nombre_productos,
            'stock_productos': stock_productos,
            'precio_productos': precio_productos
        })
        print('''
        ================================
            Nuevo producto agregado
        ================================
        ''')
        self.all_productos()

    def update_producto(self, id_productos):
        nombre_productos = input_data('Ingrese el nuevo nombre del producto >> ')
        stock_productos = input_data('Ingrese el nuevo stock del producto >> ', 'int')
        precio_productos = input_data('Ingrese el nuevo precio del producto >> ')
        self.producto.update_producto({
            'id_productos': id_productos
        }, {
            'nombre_productos': nombre_productos,
            'stock_productos': stock_productos,
            'precio_productos': precio_productos
        })
        print('''
        ============================
            Producto Actualizado
        ============================
        ''')

    def delete_producto(self, id_productos):
        self.producto.delete_producto({
            'id_productos': id_productos
        })
        print('''
        =========================
            Producto Eliminado
        =========================
        ''')

    def assign_factura(self, id_productos, producto):
        print(f'\n Asignación de facturas para el producto : {producto[1]}')
        print('''
        ==========================
            Facturas Disponibles
        ==========================
#        ''')
#        facturas = self.factura.get_factura('id_factura')
#        facturas_disponibles = []
#        if facturas:
#            for factura in facturas:
#                id_factura = factura[0]
#                nombre_factura = factura[1]
#                cursos_profesor = self.profesor_curso.search_profesor_curso({
#                    'id_profesor': profesor_id,
#                    'id_curso': curso_id
#                })
#                if not cursos_profesor:
#                    cursos_disponibles.append({
#                        'ID': curso_id,
#                        'Factura Disponible': nombre_curso
#                    })
#
#        print(print_table(cursos_disponibles))
#        curso_seleccionado = input_data(f'\nIngrese el ID del factura a asignar >> ', 'int')
#        buscar_curso = self.factura.get_curso({'curso_id': curso_seleccionado})
#        if not buscar_curso:
#            print('\nEste factura no existe !')
#            return
#        
#       
#        print('''
#        ========================
#            Factura Asignado
#        ========================
#        ''')
