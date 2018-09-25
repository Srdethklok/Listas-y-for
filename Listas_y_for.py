mi_lista = []
input_usuario = ""

input_usuario = input("que mas añadir a la lita (escribe fin para salir): ")

while input_usuario != "fin":
    mi_lista.append(input_usuario)

    if input_usuario != "fin":
        input_usuario = input("que mas añadir a la lita (escribe fin para salir): ")


largo_lista = len(mi_lista)   #`len´sirve para saver el largo de una lista
indice_actual = 0


while indice_actual < largo_lista:
    print("Tienes que {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("tu lista a finalizado")