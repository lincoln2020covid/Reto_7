from helpers.menu import Menu
from controllers.producto import ProductoController
from controllers.factura import FacturaController
from controllers.cliente import ClienteController

def app():
    try:
        print('''
        ==============================
            Sistema de facturación
        ==============================
        ''')
        menu_principal = ["Productos", "Clientes", "Facturas"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            producto = ProductoController()
            producto.menu()
            if producto.salir:
                app()
        elif respuesta == 2:
            cliente = ClienteController()
            cliente.menu()
            if cliente.salir:
                app()
        elif respuesta == 3:
            factura = FacturaController()
            factura.menu()
            if factura.salir:
                app()
        
        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

app()