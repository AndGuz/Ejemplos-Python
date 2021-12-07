import os
import time

def limpiar():
    os.system("cls" if os.name is "nt" else "clear")

def porcentaje(valor,sueldo) -> float:
    por = sueldo * (valor / 100)
    return por

def main():
    pass

if __name__ == "__main__":
    main()