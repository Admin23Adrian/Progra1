# --- ESTRUCTURA DE UNA FUNCION --- #
# def nombre(parametros):
    # instrucciones ...

# - Solo se permiten letras, numeros y guion bajo.
# - No pueden comenzar con un numero.
# - No pueden coincidir con las palabras reservadas del lenguaje.

# - Las funciones deben escribirse al principio del programa.
# - El programa principal debe comenzar despues de la ultima funcion.
# - Se recomienda que el programa principal comience con un comentario que lo identifique.

# - La funcion return termina la ejecucion de la funcion y devuelve un valor a quien
#   la haya llamado.
# - Cada funcion debe realizar una sola actividad.
# - NO deben leerse ni imprimirse valores dentro de una funcion.
# - Jamas debe salirse de una funcion desde el interior de un ciclo.

# --- CADENA DE DOCUMENTACION --- #

# - La cadena de documentacion (docstring) no es obligatoria
# - Debe especificar a la funcion, que tarea realiza.
# - Se encierra entre 3 comillas. Ej: """ Documentacion """
# - Este texto aparece en la consola de python al escribir help<nombre>

# Ejemplo 1: Desarrollar una funcion para calcular el factorial de un numero entero positivo.

def calcularfactorial(n):
    """Calcula el factorial de un numero"""
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Programa principal
a = int(input("Ingrese un numero entero: "))
b = calcularfactorial(a)
print("El factorial es", b)