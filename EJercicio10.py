lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
resultado = [lista[i] for i in range(len(lista)) if i not in [0, 4, 5]]
print(resultado)