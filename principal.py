#Laboratorio 5 Matematica Discreta
#Integrantes:
#- Estheban Heredia
#- Adrian Arimany 211063

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
    
      

def fermat_test(n, k):
    print("Fermat PRimality Test, for n = ", n, " and k = ", k)
    if n < 3:
        raise ValueError("n must be greater than 2")
    if n % 2 == 0:
        print(f"{n} is composite.")
        return
    if n == 3:
        print(f"{n} is prime.")
        return
    for a in range(2, min(n, k+1)):
         if pow(a, n-1, n) != 1:
            print(f"{n} is compossite (it failed with base {a}).")
            return
    print(f"{n} is probably prime (it passed {k} iterations).")

def mod_exp(base, exponente, modulo):    
    print("Modular Exponentiation for base = ", base, " exponent = ", exponente, " and modulo = ", modulo) 
    if base < 2:
        raise ValueError("base must be greater than 2")
    if exponente < 0:
        raise ValueError("exponent must be greater than 0")
    if modulo <= 2 or modulo >= base:
        raise ValueError("Modulo must be greater than 2 and less than base")
    result = pow(base, exponente, modulo)
    print(f"{result} is the result of {base}^{exponente} mod {modulo}")
    
    return result

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
            n = int(input("Write down an integer that you want to test if is prime or composite: "))
            k = int(input("Write down the number of iterations you want to do on n: "))
            try:
                fermat_test(n,k)
            except ValueError as e:
                print(f"Error: {e}, please try again.")
        elif opcion == '4':
            b = int(input("Write down the base: "))
            n = int(input("Write down the exponent: "))
            m = int(input("Write down the modulo: "))
            try:
                mod_exp(b, n, m)
            except ValueError as e:
                print(f"Error: {e}, please try again.")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
