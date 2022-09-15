def run():
    print("Hueveria")
    huevo_blanco_turno1 = 0
    huevo_blanco_turno2 = 0
    huevo_rojo_turno1 = 0
    huevo_rojo_turno2 = 0
    opcion = int(input("primer turno = 1, Segundo turno = 2, Sacar cuentas = 3: "))
    while opcion < 4:
        if opcion == 1:
            color_huevo = input("Que color es el huevo? ")
            if color_huevo == 'rojo':
                huevo_rojo_turno1 += 1
                print('hay '+str(huevo_rojo_turno1) + ' rojos \n')
                opcion = int(input("primer turno = 1, Segundo turno = 2, Sacar cuentas = 3: "))
            else:
                huevo_blanco_turno1 += 1
                print('hay '+str(huevo_blanco_turno1) + ' blancos \n')
                opcion = int(input("primer turno = 1, Segundo turno = 2, Sacar cuentas = 3: "))
        elif opcion == 2:
            color_huevo = input("Que color es el huevo? ")
            if color_huevo == 'rojo':
                huevo_rojo_turno2 += 1
                print('hay '+str(huevo_rojo_turno2) + ' rojos \n')
                opcion = int(input("primer turno = 1, Segundo turno = 2, Sacar cuentas = 3: "))
            else:
                huevo_blanco_turno2 += 1
                print('hay '+str(huevo_blanco_turno2) + ' blancos \n')
                opcion = int(input("primer turno = 1, Segundo turno = 2, Sacar cuentas = 3: "))
        elif opcion == 3:
            total_huevos_rojo = huevo_rojo_turno1+huevo_rojo_turno2
            total_huevos_blancos = huevo_blanco_turno2+huevo_blanco_turno1
            ganancias_turno1 = huevo_blanco_turno1*150 + huevo_rojo_turno1*200
            ganancias_turno2 = huevo_blanco_turno2*150 + huevo_rojo_turno2*200
            total_ganancias = ganancias_turno1+ganancias_turno2
            print('total huevos rojos en turno 1: '+str(huevo_rojo_turno1)+'\n total huevos blancos turno 1: '+str(huevo_blanco_turno1)+ '\n total huevos rojos en turno 2: '+str(huevo_rojo_turno2)+'\n total huevos blancos turno 2: '+str(huevo_blanco_turno2))
            print('Hay un total de '+str(total_huevos_rojo)+' huevos rojos y un total de '+str(total_huevos_blancos)+' huevos blancos\n')
            print('Ganancias del primer turno: '+str(ganancias_turno1)+ '\n Ganancias segundo turno: '+str(ganancias_turno2)+'\n Ganancias totales: '+str(total_ganancias)+' $')
            opcion=4

if __name__ == "__main__":
    run()