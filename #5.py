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
        self.lado_A = lado_A
        self.lado_B = lado_B
        self.lado_C = lado_C
        self.base = base
        self.altura = altura
    
    def calc_perim_tri(self) -> float: 
        return float(self.lado_a+self.lado_b+self.lado_c)
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
4-)Salir"""))

    if op == 1:
        pass
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        pass
    else:
        limpiar()
        menu()

if __name__ == "__main__":
    menu()