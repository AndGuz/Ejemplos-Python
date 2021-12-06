import os
import time

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("Calculador de promedio. ")
    op = input("""
    1-) Calcular promedio de 4 numeros.
    2-) Salir...  """)

    if op == "1":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        n3 = float(input("Tercer numero: ")) 
        n4 = float(input("Cuarto numero: "))

        prom = (n1+n2+n3+n4) / 4.0
        print(f"El promedio es: {prom}")
    elif op =="2":
        print("Gracias!")
        time.sleep(2)
        os._exit(0)
    else:
        print("Opcion erronea, regresando al menú...")
        time.sleep(3)
        limpiar()
        menu()


if __name__ == "__main__":
    menu()
