# from d_Menu.menu_salones import MenuSalones
from menu.menu_productos import MenuProductos
# from d_Menu.curso_menu import MenuCurso
# from d_Menu.menu_profesores import Menuprofesor
# from d_Menu.menu_periodo import MenuPeriodo
# from d_Menu.menu_profesor_curso import Menuprofesor_curso
# from d_Menu.malla_curricular_menu import MenuMallaCurricular
# from d_Menu.notas_menu import MenuNotas

class Inicio:

    def menu(self):
        while True:
            print('''
                Menú:
                1) Ir a -> Productos
                2) Ir a -> Clientes 
                3) Ir a -> Registro de ventas
                4) SALIR
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                productos = MenuProductos()
                productos.menu_productos()
            elif opcion == '2':
                menuCurso=MenuClientes()
                menuCurso.menu_clientes()
            elif opcion == '3':
                menuprofesor=MenuRegistroVentas()
                menuprofesor.menu_registro_ventas()
            elif opcion == '9':
                break
            else:
                print('No escogiste una opción valida')

inicio_objecto = Inicio()
inicio_objecto.menu()