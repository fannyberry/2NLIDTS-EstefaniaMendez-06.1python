capacidad = 10
elementos = [0] * capacidad
tope = -1
CLAVE = -1

print("Teclea elementos de la pila (termina con -1)")

while True:
    entrada = input(">> ")

    # Verificar si la entrada es un número entero
    try:
        x = int(entrada)
    except ValueError:
        print("Excepción: Entrada no válida")
        break

    # Caso de finalización
    if x == CLAVE:
        print("Finalizado con -1")
        break

    # Insertar en la pila
    if tope < capacidad - 1:
        tope += 1
        elementos[tope] = x
    else:
        print("Excepción: Pila llena")
        break

# Mostrar elementos de la pila
if tope >= 0:
    print("Elementos de la Pila:", end=" ")
    while tope >= 0:
        print(elementos[tope], end=" ")
        tope -= 1
else:
    print("Pila vacía")

