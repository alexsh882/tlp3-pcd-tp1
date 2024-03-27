"""
Un espiral numérico es una cuadrícula infinita cuyo cuadrado superior izquierdo tiene el número 1.
Tu tarea es descubrir el número en la fila x y la columna y.
"""

def number_spiral(row, column):
    # Si la fila y la columna son iguales, el número en esa posición es el cuadrado de la fila menos la fila más uno más uno.
    if row == column:
        return row**2 - row + 1
    
    # Si la fila es mayor que la columna, se verifica si la fila es par o impar. 
    # Si es par, el número en esa posición es el cuadrado de la fila menos la columna más uno.
    # Si es impar, el número en esa posición es el cuadrado de la fila menos uno más la columna.

    # Si la columna es mayor que la fila, se verifica si la columna es par o impar.
    # Si es par, el número en esa posición es el cuadrado de la columna menos uno más la fila.
    # Si es impar, el número en esa posición es el cuadrado de la columna más uno menos la fila.
    if row > column:
        if row % 2 == 0:
            return row**2 - column + 1
        else:
            return (row - 1)**2 + column
    else: 
        if column % 2 == 0:
            return (column - 1)**2 + row
        else:
            return column**2 + 1 - row

assert number_spiral(1, 5) == 25, "Error en el caso de prueba"

print("Ejercicio resuelto correctamente.")