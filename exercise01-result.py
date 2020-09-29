"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?

cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
programador:
    vaya
mente:
    no te pide nada el gusto mono


"""
# Walter Enrique Barraza Rodríguez 20180868
# creando la lista vacia
listaRegistro = []
clientes = 1
continuar = "y"
costoTotal = 0

while continuar == "y":
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(
        numClientes=clientes, cliente=cliente, producto=producto, costo=costo
    )
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    clientes += 1
    costoTotal += registro["costo"]
    continuar = input("¿Deseas continuar agregando registros? y/n ")


for registro in listaRegistro:
    print(registro)
print("El costo total hasta el momento es de " + str(costoTotal) + " dolares")
