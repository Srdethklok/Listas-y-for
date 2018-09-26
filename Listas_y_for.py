mi_lista = []
input_usuario = ""

input_usuario = input("que mas añadir a la lita (escribe fin para salir): ")

while input_usuario != "fin":
    mi_lista.append(input_usuario)

    if input_usuario != "fin":
        input_usuario = input("que mas añadir a la lita (escribe fin para salir): ")

for item in mi_lista:
    print("tienes que:{}".format(item))

print("tu lista a finalizado")