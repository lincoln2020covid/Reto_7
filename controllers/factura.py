from models.factura import Factura
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class FacturaController:
    def __init__(self):
        self.factura = Factura()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ================
                    Facturas
                ================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_facturas()
                elif respuesta == 2:
                    self.search_facturas()
                elif respuesta == 3:
                    self.insert_facturas()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_facturas(self):
        try:
            print('''
            ======================
                Lista Facturas
            ======================
            ''')
            facturas = self.factura.get_facturas('id_factura')
            print(print_table(facturas, ['ID', 'Nombre']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_factura(self):
        print('''
        ====================
            Buscar Factura
        ====================
        ''')
        try:
            id_factura = input_data("Ingrese el ID del factura >> ", "int")
            factura = self.factura.get_factura({
                'id_factura': id_factura
            })
            print(print_table(factura, ['ID', 'fecha_factura']))

            if factura:
                if question('¿Deseas dar mantenimiento al factura?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_factura(id_factura)
                    elif respuesta == 2:
                        self.delete_factura(id_factura)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_facturas(self):
        fecha_factura = input_data('Ingrese la fecha de la factura >> ')
        self.factura.insert_factura({
            'fecha_factura': fecha_factura
        })
        print('''
        ============================
            Nuevo factura agregado
        ============================
        ''')
        self.all_facturas()

    def update_factura(self, fecha_factura):
        fecha_factura = input_data('Ingrese la nueva fecha de la factura >> ')
        self.factura.update_factura({
            'id_factura': id_factura
        }, {
            'fecha_factura': fecha_factura
        })
        print('''
        ==========================
            Factura Actualizado
        ==========================
        ''')

    def delete_factura(self, curso_id):
        self.factura.delete_factura({
            'id_factura': id_factura
        })
        print('''
        ========================
            Factura Eliminado
        ========================
        ''')
