# Se te dan todos los números entre 1 a “n” excepto uno. Tu tarea es encontrar el número que falta.

def missing_number(n, arr):
    # Este calculo matemático arroja la suma de toda la serie de números, desde el 1 a n
    num = n * (n + 1) // 2
    # el método sum() suma todos los elementos de la lista ingresada
    sum_array = sum(arr)
    # Se resta la suma de la lista de números a la suma de la serie de números, arrojando el valor faltante.
    return num - sum_array

# Caso de prueba
assert missing_number(10, [1, 2, 4, 5, 6, 7, 8, 9, 10]) == 3, "Error en el caso de prueba"

print("Ejercicio resuelto correctamente.")
