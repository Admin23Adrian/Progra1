# --- PARAMETROS --- #

# - Los parametros permiten que la funcion reciba datos para hacer su trabajo.
# - Pueden pasarse de 0 a mas parametros.
# - Los parentesis son obligatorios aunque no haya ningun parametro.

# - Parametros Formales: Son los que aparecen en el encabezado de la funcion.
# - Parametros Reales: Son los que se escriben en la llamada de la funcion.

# --- Parametros Mutables. Ejemplo: --- #

def agregarTotal(lista):
    
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    lista.append(total)


miLista = [1, 2, 3, 4]

print("Lista original:", miLista)

agregarTotal(miLista)
print("Lista modificada:", miLista)