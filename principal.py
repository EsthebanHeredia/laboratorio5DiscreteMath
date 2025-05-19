#Laboratorio 5 Matematica Discreta
#Integrantes:
#- Estheban Heredia
#- Adrian Arimany

import math

def criba():
    print("Has seleccionado la Criba")
    n = int(input("Introduce un número entero positivo: "))
    if n < 2:
        print("El número debe ser mayor o igual a 2.")
        return
    lista=list(range(2, n+1))
    primos = []
    while len (lista) > 0:
        p = lista[0]
        primos.append(p)

        for i in range(p, n+1, p):
            if i in lista:
                lista.remove(i)
    print(f"Los números primos hasta {n} son: {primos}")

    
def prim_test():
    print("Deseas hacer un test de primalidad")
    n = int(input("Introduce un número entero positivo: "))
    if n < 2:
        print("El número debe ser mayor o igual a 2.")
        return
    k = math.isqrt(n)
    lista = list(range(2, k+1))
    primos = []
    while len (lista) > 0:
        p = lista[0]
        primos.append(p)

        for i in range(p, k+1, p):
            if i in lista:
                lista.remove(i)
    for j in primos:
        if n % j == 0:
            print(f"{n} no es primo, es divisible por {j}")
        else:
            print(f"{n} es primo, no es divisible por ningun número menor a su raíz cuadrada")  
        return
    
      

def fermat_test():
    print("Deseas hacer un test de primalidad de Fermat")

def mod_exp():
    print("Deseas hacer una exponenciación modular")


def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Criba")
    print("2. Test de Primalidad")
    print("3. Test de Primalidad de Fermat")
    print("4. Exponenciación Modular")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            criba()
        elif opcion == '2':
            prim_test()
        elif opcion == '3':
            fermat_test()
        elif opcion == '4':
            mod_exp()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
