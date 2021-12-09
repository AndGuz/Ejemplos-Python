import os
import time


def limpiar() -> None:
    os.system("cls" if os.name == "nt" else "clear")

#La raiz cubica se saca elevando x por la division de 1/3 que es un tercio
def qrt(x) -> float:
    return x**(1./3.)

def geo_media(n1,n2,n3) -> float:
    return qrt((n1*n2*n3))

def main() -> None:
    print("""
Hola!
Bienvenido al calculador de media geometrica. """)
    x1 = float(input("Inserte la primera variable: "))
    x2 = float(input("Inserte la segunda variable: "))
    x3 = float(input("Inserte la tercera variable: "))
    print(f"La media geometrica es: {geo_media(x1,x2,x3)}")
    time.sleep(5)
    os._exit(0)

if __name__ == "__main__":
    main()
    