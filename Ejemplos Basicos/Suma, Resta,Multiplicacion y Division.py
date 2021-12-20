# 4- Crear un programa que diga la suma, resta, multiplicación y división de dos numero enteros
import time
import os


def suma():
    var1 = float(
        input("Has elegido la suma asi que ingresa el primer numero entero: "))
    var2 = float(input("Segunda variable por favor: "))
    print("El resultado es: ", var1 + var2)
    menu()


def mult():
    var1 = float(
        input("Has elegido la multipicacion asi que ingresa el primer numero entero: "))
    var2 = float(input("Segunda variable por favor: "))
    print("El resultado es: ", var1 * var2)
    menu()


def rest():
    var1 = float(
        input("Has elegido la resta asi que ingresa el primer numero entero: "))
    var2 = float(input("Segunda variable por favor: "))
    print("El resultado es: ", var1 - var2)
    menu()


def div():
    var1 = float(
        input("Has elegido la division asi que ingresa el primer numero entero: "))
    var2 = float(input("Segunda variable por favor: "))
    print("El resultado es: ", var1 / var2)
    menu()


def eval_exp():
    exp = input(
        """Inserte expresion matematica que se puede hacer con "*,+,/,**,%" \n""")
    print("Resultado: ", eval(exp))
    menu()


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("Bienvenido a la mas cutre calculadora!")
    print("""
¿Que deseas hacer? 
1-)Multiplicar
2-)Sumar
3-)Restar
4-)Dividir
5-)Evaluar expresion
6-)Salir """)
    op = input("Opcion: \n")

    if op == "1":
        mult()
    elif op == "2":
        suma()
    elif op == "3":
        rest()
    elif op == "4":
        div()
    elif op == "5":
        eval_exp()
    elif op == "6":
        os._exit(0)
    else:
        print("Opcion erronea, regresando al menu principal...")
        time.sleep(3)
        limpiar()
        menu()


if __name__ == "__main__":
    menu()
