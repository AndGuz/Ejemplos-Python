# Autor: Anderson Guzman Abreu
# 3- Convertir un grados Celsius a Fahrenheit

#formula: F = (C * 1.8) + 32
#C = (F-32)/1.8
import time
# dira usted pa que diablo time y os, para la funcion del menu xd
import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def conv_cel_fahr(grados):
    print(str((grados * 1.8 + 32)) + " Fahrenheit")


def conv_fahr_cel(grados):
    print(str(((grados - 32)/1.8)) + " Celsius")


def menu():
    print("¿Que desea hacer? ")
    op = input("""
    1-) Convertir grados celcius a fahrenheit
    2-) Convertir grados Fahrenheit a Celcius """)

    if op == "1":
        grados_usr = float(input("¿Cuantos grados celsius son? "))
        conv_cel_fahr(grados_usr)
    elif op == "2":
        grados_usr = float(input("¿Cuantos grados fahrenheit son? "))
        conv_fahr_cel(grados_usr)
    else:
        print("Opcion erronea, regresando al menú...")
        time.sleep(3)
        limpiar()
        menu()


if __name__ == "__main__":
    menu()
