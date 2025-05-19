def criba():
    print("Has seleccionado la Criba")


def prim_test():
    print("Deseas hacer un test de primalidad")


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