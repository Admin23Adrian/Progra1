# --- PARAMETROS POR OMISION --- #

# - Escribir una funcion para calcular la raiz n-esima de un numero

def calcularRaiz(radicando, indice=2):
    return radicando ** (1/indice)

a = float(input("Ingrese el radicando: "))
r2 = calcularRaiz(a)
r3 = calcularRaiz(a, 3)

print("Raiz cuadrada:", r2)
print("Raiz Cubica:", r3)