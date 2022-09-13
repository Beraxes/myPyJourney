def esPrimo():
        pass

def run():
        numero = int(input("Escribe un numero: "))
        if esPrimo(numero):
          print("Es primo")
        else:
                print("No es primo")

if __name__=="__main__":
        run()