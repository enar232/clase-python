numero = [4, 7, 2, 4, 9, 2, 8, 6, 7]

#eliminar duplicados
sin_duplicados = list (set(numeros))
priny ("lista sin duplicados:", sin_duplicados)

#ordenar de menos a mayor
ordenada = sorted(sin_duplicados)
print("lista ordenada:", ordenada)

#mostrar solo los numeros pares 
pares = [num for num in ordenada if num % == 0]
print("numeros pares:", pares)
