from models.cliente import Cliente
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class ClienteController:
    def __init__(self):
        self.cliente = Cliente()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Clientes
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_clientes()
                elif respuesta == 2:
                    self.search_cliente()
                elif respuesta == 3:
                    self.insert_cliente()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_clientes(self):
        try:
            print('''
            ==========================
                Listar Clientes
            ==========================
            ''')
            clientes = self.cliente.get_clientes('id_clientes')
            print(print_table(clientes, ['ID', 'tipo_clientes', 'nombre_clientes']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_cliente(self):
        print('''
        ========================
            Buscar Cliente
        ========================
        ''')
        try:
            cliente_id = input_data("Ingrese el ID del cliente >> ", "int")
            cliente = self.cliente.get_cliente({
                'id_cliente': id_cliente
            })
            print(print_table(cliente, ['ID', 'Tipo', 'nombre']))

            if cliente:
                if question('¿Deseas dar mantenimiento al cliente?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_cliente(id_cliente)
                    elif respuesta == 2:
                        self.delete_cliente(id_cliente)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_cliente(self):
        tipo_cliente = input_data('Ingrese el tipo de cliente >> ')
        nombre_cliente = input_data('Ingrese el nombre del cliente >> ', 'int')
        self.cliente.insert_cliente({
            'tipo_cliente': tipo_cliente,
            'nombre_cliente': nombre_cliente
        })
        print('''
        ================================
            Nuevo cliente agregado
        ================================
        ''')
        self.all_clientes()

    def update_cliente(self, cliente_id):
        tipo_cliente = input_data('Ingrese el nuevo tipo de cliente >> ')
        nombre_cliente = input_data('Ingrese el nuevo nombre del cliente >> ', 'int')
        self.cliente.update_cliente({
            'id_cliente': id_cliente
        }, {
            'tipo_cliente': tipo_cliente,
            'nombre_cliente': nombre_cliente
        })
        print('''
        ============================
            Cliente Actualizado
        ============================
        ''')

    def delete_cliente(self, id_cliente):
        self.cliente.delete_cliente({
            'id_cliente': id_cliente
        })
        print('''
        =========================
            Cliente Eliminado
        =========================
        ''')

