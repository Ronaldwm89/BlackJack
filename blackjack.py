import random
import artblack

cartas = {
    "♥️": ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
    "♦️": ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
    "♠️": ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
    "♣️": ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
} #Diccionario con todas las barajas del juego

def eliminar_carta(simbolo, cards, indice):
    if simbolo in ["♥️","♦️","♠️","♣️"]:
        if indice == 11:
            indice = "J"
        elif indice ==12:
            indice = "Q"
        elif indice ==13:
            indice = "K"
        elif indice == 0:
            indice= "A"
        
        if indice in cards:
            cartas[simbolo].remove(indice)#Elimina la carta ya escogida de la baraja original         

def simbolo_y_carta(symbol, card):#Elige una carta aleatoria dentro de la baraja
    simbolo = random.choice(list(cartas))
    carta = random.choice(cartas[simbolo])

    lista_cartas = list(cartas[simbolo])
    indice_carta = lista_cartas.index(carta)

    symbol.append(simbolo)
    card.append(carta)

    eliminar_carta(simbolo, lista_cartas, indice_carta)

def eleccion_carta_pc():#Elige una carta para el PC
    simbolo_y_carta(simbolos_pc, cartas_pc)

    cartas_del_pc = [f"{s}{c}" for s, c in zip(simbolos_pc, cartas_pc)]
    print(f"Las cartas del PC son: {cartas_del_pc}")
    
def valor_carta(carta):#Asigna el valor correcto a cartas especiales
    if carta in ["J","Q","K",]:
        return 10
    elif carta == "A":
        return 11
    else:
        return carta

def total_cards(cartas):#Suma el valor real de cada carta y los almacena
    total = 0
    ases = 0

    for carta in cartas:
        valor = valor_carta(carta)
        total += valor
        if carta == "A":
            ases += 1
    
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total

def eleccion_carta():#Elige una carta para el Usuario
    simbolo_y_carta(simbolos_user, cartas_user)

def juega_pc(valor_usuario):#Acciones de juego del pc
    total_pc = total_cards(cartas_pc)
    while total_pc < 16 or (valor_usuario > total_pc and valor_usuario <= 21):  #4 < 14
        eleccion_carta_pc()
        total_pc = total_cards(cartas_pc)
        print(f"Y en total suman: {total_pc}")

        if total_pc < 16 or (valor_usuario > total_pc and valor_usuario <= 21):
            print("\n")
            print("La pc elige otra carta: ")
      
        if total_pc == 21 and valor_usuario < 21:
            
            print("Lo sentimos perdiste el juego ♥️♦️♠️♣️😢")
        
        if total_pc < 21 and total_pc > valor_usuario:
            
            print("Lo sentimos perdiste el juego ♥️♦️♠️♣️😢")
        
        if total_pc > 21:
            print(f"El usuario ha ganado 😉 porque el PC obtuvo un total de: {total_pc}")
      
        elif total_pc == valor_usuario:
            print(f"Ha sido un empate los dos han obtenido {total_pc}")
        
def nueva_carta():#Acciones de juego del usuario
    seguir_jugando = True
    while seguir_jugando:
        print("\n")
        otra_carta = input("¿Deseas pedir otra carta? S/N : \n").upper()
        if otra_carta == "S":
            eleccion_carta()
            total_cartas = total_cards(cartas_user)
            tus_cartas = [f"{s}{c}" for s, c in zip(simbolos_user, cartas_user)]
            print(f"Tus cartas actuales son: {tus_cartas} \n y en total suman: {total_cartas}") 
            if total_cartas > 21:
                print("Lo sentimos perdiste el juego ♥️♦️♠️♣️😢")
                break
            elif total_cartas == 21:
                print("Has llegado a 21, no deberias pedir mas cartas")
        elif otra_carta == "N":
            total_cartas = total_cards(cartas_user)
            print("\n")
            print(f"Paraste con {total_cartas}")
            juega_pc(total_cartas)
            seguir_jugando = False     
        else:
            print("Opción no válida, por favor ingresa 'S' o 'N'.")

# Inicializa el juego
exit = True
while exit:
    salida = input("Desea Jugar al BlackJack? S/N: ").upper()
    if salida == 'S':
        simbolos_user = []
        cartas_user = []
        cartas_pc = []
        simbolos_pc = []

        print(artblack.logoblack)
        print("Bienvenido a nuestro juego: \n")
        eleccion_carta()  # Obtén las primeras dos cartas
        eleccion_carta()

        total_cartas = total_cards(cartas_user)
        tus_cartas = [f"{s}{c}" for s, c in zip(simbolos_user, cartas_user)]
        print(f"Tus cartas iniciales son: {tus_cartas} \n y en total suman: {total_cartas}")
        print("\n")

        eleccion_carta_pc() #Primera carta del pc

        nueva_carta()

        exit = True
    
    if salida == 'N':
            print("Adios, hasta una proxima!!")
            exit = False
    else:
        print("Debes elegir una opcion valida entre S/N")
        exit = True
































