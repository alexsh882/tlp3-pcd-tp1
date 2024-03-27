"""
Dada una cadena de caracteres, tu tarea es reorganizar los caracteres de la cadena de manera
que puedas formar un palíndromo. Si no es posible formar un palíndromo, debes indicarlo.
"""

# Defino la función que recibirá la palabra que queremos intentar ordenar
def palindrome_reorder(word):
    # Seteo las palabras, de modo que no me se repitan las letras
    setLetters = set(word)
    # Ordeno la palabra ingresada de manera descendente
    setLetters = sorted(setLetters, reverse=True)
    # Creo un array para almacenar el resultado de las operaciones
    palindrome = []
    # Creo un boleano, al cual se le asignara el valor True cuando se encuentre la letra central
    is_letter_odd = False
    # Ejecuto un ciclo for con las letras seteadas
    for letter in setLetters:
        # compruebo si cada letra del ciclo se repite y la repetición es par
        if word.count(letter) % 2 == 0:
            # realizo un ciclo for por la cantidad de veces que se repita la letra.
            for _ in range(word.count(letter) // 2):
                # Agrego al principio y al final la letra que se repite.
                palindrome.insert(0, letter)
                palindrome.append(letter)
        else:
            #Si la letra se encuentra solo una vez dentro de la palabra ingresada:

            # agregue una clausula de guarda para evitar que se agreguen más palabras al centro, en caso de que eso suceda.
            if is_letter_odd:
                return "NO SOLUTION"
            # Si para la clausula anterior, se inserta en el medio de la lista la letra solitaria.
            palindrome.insert(len(palindrome) // 2, letter)
            # una vez agregada, se asigna el valor True al boleano.
            is_letter_odd = True
    # retornamos como string la lista generada.
    return "".join(palindrome)

#Casos de prueba
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
assert palindrome_reorder("aqiowue") == "NO SOLUTION", "Error en el caso de prueba"

print("Ejercicio resuelto correctamente.")
