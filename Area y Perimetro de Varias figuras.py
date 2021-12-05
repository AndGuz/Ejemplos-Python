#5 Crea un programa que calcule el área y el perímetro de un triangulo
import os
import time
import cmath
#Importé cmath porque se que tiene una variable de pi bien completa (gracias blender)
def limpiar():
    os.system("cls" if os.name=="nt" else "clear")

class Triangulo:
    #El perimetro es la suma de sus tres lados mientras el area es la base por la altura entre 2, A=B * a / 2
    def __init__(self,lado_A,lado_B,lado_C,base,altura) -> None:
        #Variables fundamentales
        self.lado_A = lado_A
        self.lado_B = lado_B
        self.lado_C = lado_C
        self.base = base
        self.altura = altura
    #sumar sus lados esta bien para cualquier triangulo
    def calc_perim_tri(self) -> float: 
        return float(self.lado_A+self.lado_B+self.lado_C)
    #el area es la base por la altura entre dos, se autoexplica
    def calc_area_tri(self) -> float:
        return float((self.base*self.altura)/2.0)

class Cuadrado:
    def __init__(self,lado) -> None:
        self.lado = lado
    def calc_perim_cuad(self) -> float:
        return(self.lado * 4.0)
    def calc_area_cuad(self) -> float:
        return(self.lado ** 2.0)

class Circulo:
    def __init__(self,radio) -> None:
        self.radio = radio
    def calc_perim_cir(self) -> float:
        return(2*cmath.pi*self.radio)
    def calc_area_cir(self) -> float:
        return(cmath.pi * self.radio**2.0)
        
def menu():
    print("""Bienvenido al calculador de area y perimetro de triangulos, cuadrados y circulos.""")
    op= int(input("""
¿Que desea hacer?
1)Perimetro y Area de un triangulo.
2-)Perimetro y Area de un Cuadrado.
3-)Perimetro y Area de un Circulo.
4-)Salir... """))

    if op == 1:
        l1 = int(input("Inserte la medida del lado A, nótese que deben ser de la magnitud. EG: cm. "))
        l2 = int(input("Lado B: "))
        l3 = int(input("Lado C: "))
        b = int(input("Base: "))
        a = int(input("Altura: "))

        tri = Triangulo(l1,l2,l3,b,a)

        print(f"El perimetro es: {tri.calc_perim_tri()} ")
        print(f"El area de ese triangulo es: {tri.calc_area_tri()} ")
        print("Retornando al menu...")
        time.sleep(2)
        #Debo eliminar las variables ya que puedo introducir a un memory escape
        del tri,l1,l2,l3,b,a
        menu()

    elif op == 2:
        l= int(input("Inserte la medida de un lado (calcula cuadrados perfectos): "))
        
        quad = Cuadrado(l)

        print(f"El area es: {quad.calc_area_cuad()}. ")
        print(f"El perimetro es: {quad.calc_perim_cuad()}. ")
        print("Retornando al menu...")
        time.sleep(2)

        del l,quad
        menu()
    elif op == 3:
        r = int(input("Inserte la medida del radio: "))
        
        cir = Circulo(r)

        print(f"El area es: {cir.calc_area_cir()}. ")
        print(f"El perimetro es: {cir.calc_perim_cir()}. ")
        print("Retornando al menu...")
        time.sleep(2)

        del r,cir
        menu()
    elif op == 4:
        print("Gracias por usarme!")
        os._exit(0)
    else:
        print("Seleccionaste una opcion no existente.. ")
        time.sleep(5)
        limpiar()
        menu()

if __name__ == "__main__":
    menu()