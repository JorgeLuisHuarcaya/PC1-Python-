consumo = float(input("¿Cuánto fue tu consumo? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dejar? "))
propina = consumo * (porcentaje_propina / 100)
print(f"La propina es: {propina}")