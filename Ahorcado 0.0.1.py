import random

def display(letra, palabra, guiones):
    for i in range(len(palabra)):
        if letra == palabra[i]:
            guiones[i] = letra
            continue
    return str(guiones)
            
def ahorcado():
    test = ("1234567890")
    numero = random.randint(1,103) 
    palabras = ("torta pegamento computadora otorrinolaringologo oftalmologo teclado pizza anana pieza carpeta llaves barba abrigo camisa remera billetera calculadora dedos ojos nariz dientes labios luz oso jirafa elefante plato alcohol globo cuchara tenedor cuchillo internet barco carpa auriculares papas lechuga tomate zapatillas plantillas cordones cuaderno psicologo doctor abogado enfermero materia sinonimo bolsa lampara aula pipa procesador huevos jamon leche pan azucar sal llavero papel lapiz lapicera cartuchera alfajor chocolate blanco negro azul rojo cuadrado circulo triangulo pastel cajon armario mesa silla gorra cinta pizarra bastidor impresora techo piso escalera planta ojota alpargata regla funda guitarra piano trapecio omoplato falange sangre madera metal vinilo lente pichula").split()
    palabra = palabras[numero]
    vidas = 8
    letras_adivinadas = []
    letras_no_adivinadas = []
    guiones = []
    for i in range(len(palabra)):
        guiones.append("_")
    print("")
    print("")
    print("Ya pensé mi palabra, tiene ", str(len(palabra)), " letras.")
##    print("Pssst developer, la palabra es: ", palabra)

    while vidas > 0 and palabra != "".join(guiones):
        print(guiones)
        print("")
        letra = input("Escribi tu letra:  ")

        if len(letra) != 1:
            print("")
            print("Escribí UNA letra")
            continue

        elif letra in test:
            print("")
            print("Escribí una LETRA")
            continue

        elif letra in letras_no_adivinadas:
            print("")
            print("Ya usaste esta letra :(, intenta con otra")

        elif letra in palabra:
            letras_adivinadas.append(letra)
            print("")
            print("Correcto!")
            print("Tu palabra hasta el momento:", display(letra, palabra, guiones))
            print("Letras correctas = " + str(letras_adivinadas))
            print("Letras incorrectas = " + str(letras_no_adivinadas))
            print("Te quedan: ", vidas, "vidas")

        elif letra not in palabra:
            vidas = vidas - 1
            letras_no_adivinadas.append(letra)
            print("")
            print("Incorrecto!")
            print("Tu palabra hasta el momento:", display(letra, palabra, guiones))
            print("Letras correctas = " + str(letras_adivinadas))
            print("Letras incorrectas = " + str(letras_no_adivinadas))
            print("Te quedan: ", vidas, "vidas")
            
    if palabra == "".join(guiones):
        print("")
        print("Adivinaste! Felicitaciones, querés volver a jugar?")
        rta = input("si/no  ")
        if rta == "si":
            ahorcado()
        elif rta == "no":
            print("")
            print("Ok, byebye :)")
            print("")
            print("")
            print("")
            exit()
            

    elif vidas == 0:
        print("")
        print("jaja perdiste contra un mediocre script")
        print("La palabra era: ", palabra)
        print("querés volver a intentarlo?")
        rta = input("si/no")

        if rta == "si":
            ahorcado()

        elif rta == "no":
            print("")
            print("Ok, byebye :)")
            print("")
            print("")
            print("")
            exit()
        

        
### INIT
            
while True:
    print("Bienvenidx al ahorcado, necesitas instrucciones?")
    rta = input("si/no  ")

    if rta == "no":
        ahorcado()
        
    elif rta == "si":
        print("")
        print('''El juego es muy fácil, yo pienso en una palabra y te digo el número de letras que tiene.
Luego vos escribís una letra, si esta letra se encuentra en la palabra, yo la descubro y volvés a escribir una letra.
Si por otro lado, no adivinas, perdes una de las 8 vidas que tenés. Volvés a intentarlo hasta ganar o perder :).''')
        print("")
        print("Jugamos?")
        print("")
        rta = input("si/no")

        if rta == "si":
            ahorcado()
                

        elif rta == "no":
            print("")
            print("Ok morite >:( ")
            exit()

    
         
