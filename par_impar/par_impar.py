entrada = int(input("¿En qué número estás pensando (1 - 1000)?: "))

# Esta función es para verificar que el número de entrada sea un número par o impar
def par_impar(entrada):
    if entrada % 2 == 0:
        print("Ese número que seleccionaste es par ")
    else:
        print("Ese número que seleccionaste es impar")


par_impar(entrada)