mi_lista = []
input_usuario = ""

while input_usuario != "FIN":
    input("que mas añadir a la lita (escribe FIN para salir): ")
    mi_lista.append(input_usuario)

largo_lista = len(mi_lista)   #`len´sirve para saver el largo de una lista
indice_actual = 0


while indice_actual < largo_lista:
    print("Tienes que {}".format(mi_lista[indice_actual]))
    indice_actual += 1