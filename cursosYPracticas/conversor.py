def conversorUSD(tipo_moneda, dolar_hoy):
    pesos = float(input("Cuantos pesos " + tipo_moneda + " tienes?: "))
    dolares = pesos / dolar_hoy
    dolares = round(dolares, 2)
    print("tienes: $ "+str(dolares)+" Dolares")

opcion = int(input("Ingrese Opcion \n 1:Convertir COP a USD 2: Convertir ARS a USD 3:Salir\n"))

while opcion != 3 and opcion < 4:
    if opcion==1:
      conversorUSD("COP", 4307)
      opcion = int(input("Ingrese Opcion \n 1:Convertir COP a USD 2: Convertir ARS a USD 3:Salir\n"))
    elif opcion == 2:
        conversorUSD("ARS", 65)
        opcion = int(input("Ingrese Opcion \n 1:Convertir COP a USD 2: Convertir ARS a USD 3:Salir\n"))