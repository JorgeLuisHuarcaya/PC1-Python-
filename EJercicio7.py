num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("Elige una opción: 1. Sumar 2. Restar 3. Multiplicar")
opcion = int(input("Introduce el número de la opción: "))

if opcion == 1:
    print(f"La suma es: {num1 + num2}")
elif opcion == 2:
    print(f"La resta es: {num1 - num2}")
elif opcion == 3:
    print(f"La multiplicación es: {num1 * num2}")
else:
    print("Opción no válida")