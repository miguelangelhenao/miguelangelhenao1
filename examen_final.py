

entrada = input("Ingresa una lista de números enteros separados por comas: ")

numeros_str = entrada.split(',')

numeros = [int(num.strip()) for num in numeros_str]

numero_mas_grande = max(numeros)

veces_apariciones = numeros.count(numero_mas_grande)

print(f"El número más grande en la lista es: {numero_mas_grande}")
print(f"Aparece {veces_apariciones} {'vez' if veces_apariciones == 1 else 'veces'} en la lista.")



