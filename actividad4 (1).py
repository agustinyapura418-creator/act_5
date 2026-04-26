# ============================================================
# Actividad N°4 - Taller de Programacion
# Importa todos los modulos desde procesos.py
# ============================================================

from procesos import (
    ejercicio1,
    ejercicio2,
    ejercicio3,
    ejercicio4,
    ejercicio5,
    ejercicio6,
    ejercicio7,
    ejercicio8,
    ejercicio9,
    ejercicio10
)

# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal():
    while True:
        print("\n========== ACTIVIDAD 4 ==========")
        print("1.  Maximo entre tres numeros")
        print("2.  Maximo entre diez numeros")
        print("3.  Operaciones con vectores")
        print("4.  Contar vocales y consonantes")
        print("5.  Menu potencia/digitos/capicua")
        print("6.  Suma o producto de matrices")
        print("7.  Matriz cuadrada y diagonal")
        print("8.  Electrodomesticos")
        print("9.  Lista de pacientes")
        print("10. Maquina tragamonedas")
        print("0.  Salir")

        op = input("\nElegir ejercicio: ")

        if op == "1":
            ejercicio1()
        elif op == "2":
            ejercicio2()
        elif op == "3":
            ejercicio3()
        elif op == "4":
            ejercicio4()
        elif op == "5":
            ejercicio5()
        elif op == "6":
            ejercicio6()
        elif op == "7":
            ejercicio7()
        elif op == "8":
            ejercicio8()
        elif op == "9":
            ejercicio9()
        elif op == "10":
            ejercicio10()
        elif op == "0":
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

menu_principal()
