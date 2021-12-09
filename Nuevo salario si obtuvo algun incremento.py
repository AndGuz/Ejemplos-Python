import os
import time

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def porcentaje(valor,sueldo) -> float:
    por = sueldo * (valor / 100)
    return por

def main():
    limpiar()
    sueldo_act = float(input("Inserte salario actual: "))
    porc = float(input("Inserte incremento de porciento: "))
    sueldo_nuev = porcentaje(porc,sueldo_act) + sueldo_act
    print(f"Su sueldo sera de: {sueldo_nuev}. ")
    time.sleep(5)
    os._exit(0)

if __name__ == "__main__":
    main()
    