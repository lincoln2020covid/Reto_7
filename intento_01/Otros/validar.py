import re
from models.productos import ModelProductos

class Validacion:
    def __init__(self):
        self.productos=ModelProductos()


    def validar_nota(self):
        while True:
            try:
                while True:
                    nota=float(input(f"Ingrese la nota:\n"))
                    if nota>=0 and nota<=20:
                        break
                    else:
                        print("Ingrese una nota entre 0 a 20")
                break
            except ValueError:
                print(f'Ingrese un numero valido')
        return nota
    @classmethod
    def validar_texto(cls,Comentario):
        texto=""
        while True:
            texto=input(f"{Comentario}:\n")
            if cls.validar_palabra_alfabetico(texto):
                return texto
                  
            else:
                print("Error-El texto ingresado contiene caracteres numericos")

    @staticmethod
    def validar_palabra_alfabetico(texto):
        valor_de_verdad=True
        lista_texto=texto.split(" ")
        for palabra in lista_texto:
            if palabra.isalpha():
                valor_de_verdad=True  
            else:
                valor_de_verdad=True
        return valor_de_verdad
    @staticmethod
    def validar_stock(Comentario):
        stock_productos=''
        while True:
            try:
                while True:
                    stock_productos=int(input(f"{Comentario}:\n"))
                    if stock_productos>=0:
                        return stock_productos
                    else:
                        print("Error-Ingrese stock igual o mayor a cero")
                break
            
            except ValueError:
                print(f'Error-Ingrese un numero valido')
    @staticmethod
    def validar_precio(Comentario):
        precio_producto=''
        while True:
            try:
                while True:
                    precio_producto=float(input(f"{Comentario}:\n"))
                    if precio_producto>0:
                        return precio_producto
                    else:
                        print('Ingrese valores positivos')
                break
                
            except ValueError:
                    print("Precio ingresado no válido")

    def validar_id_producto(self,codigo_ingresado):
        id_productos=self.productos.get_all_productos('id_producto')
        valor=False
        for id_producto in id_productos:
            if(id_producto==codigo_ingresado):
                valor=True
        return valor
