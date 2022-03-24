# Ejemplo:

cuadrado = lambda x: x ** 2
print(cuadrado(3))

# Todo lo que este antes de : son los parametros.
# Todo lo que este despues de los : es el valor que devuelve.

# -- Sintaxis -- #
# <var> = lambda <parametros> : <valor de retorno>

# Ejemplo con dos parametros:

raiz = lambda x, y : x ** (1/y)
print("La raiz es:", raiz(27, 3))

# Tambien se pueden asignar parametros por omision:
raiz3 = lambda x, y = 3 : x ** (1 / y)
print(raiz3(27))