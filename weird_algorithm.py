"""
Considera un algoritmo que toma como entrada un entero positivo n. Si n es par, el algoritmo
lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y le suma uno. El
algoritmo repite esto hasta que n sea uno.
"""

def weird_algorithm(n):
    # Creo una variable para acumular el resultado
    result = [n]
    # utilizo el ciclo while, mientras el valor ingresado sea diferente de 1
    while n != 1:
        # Si el valor ingresado es par
        if n % 2 == 0:
            # Divido el valor ingresado entre 2 y reasigno el valor a la variable n
            n = n // 2
            # Agrego el valor a la lista result
            result.append(n)
        else:
            #Si el valor ingresado es impar
            #multiplico el valor ingresado por 3 y le sumo 1
            n = n * 3 + 1
            # Agrego el valor a la lista result
            result.append(n)
    # Retorno la lista con el resultado final
    return result


assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print("Ejercicio resuelto correctamente.")
