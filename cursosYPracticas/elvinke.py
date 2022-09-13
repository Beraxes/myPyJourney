nombres = []
apellidos = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 0
# Leemos los datos y los agregamos a la lista
opcion = int(input("Quieres Agregar usuarios?? Si=1 No=0 "))
while opcion==1:
        print("Ingrese los datos de la persona")
        nombre = input("Nombre: ")
        apellido = input("apellido: ")
        identificación = input("Identificación: ")
        nombres.append(nombre)
        apellidos.append(apellido)
        identificaciones.append(identificación)
        tamaño= tamaño+1
        opcion = int(input("Quires seguir agregando usuarios? Si=1 No=0  "))
        
print("\n")

# Ahora mostremos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona")
    print("Nombre:", nombres[i])
    print("apellido:", apellidos[i])
    print("Identificación:", identificaciones[i])
    print("___________________________________")