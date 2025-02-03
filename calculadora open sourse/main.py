from sumar import sumar
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar varios números")
    print("6. Salir")

def obtener_numero():
    while True:
        try:
            numero = float(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1-6): ")

        if opcion == "1":
            num1 = obtener_numero()
            num2 = obtener_numero()
            print(f"La suma es: {sumar(num1, num2)}")
        elif opcion == "2":
            num1 = obtener_numero()
            num2 = obtener_numero()
            print(f"La resta es: {resta(num1, num2)}")
        elif opcion == "3":
            num1 = obtener_numero()
            num2 = obtener_numero()
            print(f"La multiplicación es: {multiplicar(num1, num2)}")
        elif opcion == "4":
            num1 = obtener_numero()
            num2 = obtener_numero()
            if num2 != 0:
                print(f"La división es: {dividir(num1, num2)}")
            else:
                print("No se puede dividir por cero.")
        elif opcion == "5":
            cantidad = int(input("¿Cuántos números quiere sumar? "))
            numeros = []
            for _ in range(cantidad):
                num = obtener_numero()
                numeros.append(num)
            print(f"La suma de los números es: {suma_avanzada(numeros)}")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor elija una opción entre 1 y 6.")

if __name__ == "__main__":
    main()
