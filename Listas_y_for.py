mi_lista = ["despertar", "desayunar", "salir a trabajar", "trabajar", "salir del trabajo"]

largo_lista = len(mi_lista)   #`len´sirve para saver el largo de una lista
indice_actual = 0


while indice_actual < largo_lista:
    print("Tienes que {}".format(mi_lista[indice_actual]))
    indice_actual += 1