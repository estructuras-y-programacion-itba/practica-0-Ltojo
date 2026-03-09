import random

def sumar_lista(lista): #lista de punajes
    puntaje = 0
    for elemento in lista:
        puntaje += elemento
    return puntaje

def ganador(lista_p1, lista_p2): #listas de puntajes

    puntaje_jugador_1 = sumar_lista(lista_p1)

    puntaje_jugador_2 = sumar_lista(lista_p2)

    if puntaje_jugador_1 > puntaje_jugador_2:
        print('gana el jugador 1')
    elif  puntaje_jugador_1 < puntaje_jugador_2:
        print("gana el jugador 2")
    else:
        print("es un empate")
    


def tirar(num):
    i = 0
    lista_tirada = []
    while i < num:
        numero = random.randint(1, 6)
        lista_tirada.append(numero)
        i += 1
    return lista_tirada

def jugador1(lista_cat_usados1, puntajes1):
    lista_cat = ['1', '2', '3', '4', '5', '6', "E", "F", 'G', "P"]
    terminar = False
    lista_conservados = []
    contador = 0
    finalizar_turno = False
    
    while contador < 3:
        if finalizar_turno == False:
            tiradas = tirar(5 - len(lista_conservados))
            print(tiradas)

            for elem in tiradas:
                dec = input(f'Desea guardar {elem} ? S/N: ')
                if dec == "S" or dec == "s":
                    lista_conservados.append(elem)

            print(lista_conservados)

            if contador == 2:
                pun = "S"
            else:
                pun = input("Desea finalizar: ")
            punt1 = 0
            if pun == "s" or pun == "S":
                cat = input('Ingrese categoria seleccionada: ')
                if cat not in lista_cat_usados1:
                    lista_cat_usados1.append(cat)
                    if '1' <= cat <= '6':
                        
                        for num in lista_conservados:
                            if num == int(cat):
                                punt1 += num
                        puntajes1.append(punt1)
                    else:
                        if cat == 'G':
                            if contador == 0:
                                print("gana el jugador 1 por generala")
                                terminar = True
                                return 
                            else:
                                puntajes1.append(50)
                        elif cat == 'E':
                            puntajes1.append(20)
                        elif cat == 'F':
                            puntajes1.append(30)
                        elif cat == 'P':
                            puntajes1.append(40)
                finalizar_turno = True

        contador += 1

    # Completar categorias no usadas con 0
    i = 0
    while i < len(lista_cat):
        ok = False
        j = 0
        while j < len(lista_cat_usados1):
            if lista_cat[i] == lista_cat_usados1[j]:
                ok = True
            j += 1
        if ok == False:
            lista_cat_usados1.append(lista_cat[i])
            puntajes1.append(0)
        i += 1
    
    print(f'El jugador 1 puntuo {punt1}')
    return terminar

def jugador2(lista_cat_usados2, puntajes2):
    lista_cat = ['1', '2', '3', '4', '5', '6', "E", "F", 'G', "P"]
    terminar = False
    lista_conservados = []
    contador = 0

    while contador < 3:
        tiradas = tirar(5 - len(lista_conservados))
        print(tiradas)

        for elem in tiradas:
            dec = input(f'Desea guardar {elem} ? S/N: ')
            if dec == "S" or dec == "s":
                lista_conservados.append(elem)

        print(lista_conservados)
        pun = input("Desea finalizar: ")
        punt2 = 0
        if pun == "s" or pun == "S":
            cat = input('Ingrese categoria seleccionada: ')
            if cat not in lista_cat_usados2:
                lista_cat_usados2.append(cat)
                if '1' <= cat <= '6': #GONZA CAT ES UN STR SI USAS CUALQUIER ELTRA CRASHEA
                    
                    for num in lista_conservados:
                        if num == int(cat):
                            punt2 += num
                    puntajes2.append(punt2)
                else:
                    if cat == 'G':
                        if contador == 0:
                            print("gana el jugador 2 por generala")
                            terminar = True
                            return
                        else:
                            puntajes2.append(50)
                    elif cat == 'E':
                        puntajes2.append(20)
                    elif cat == 'F':
                        puntajes2.append(30)
                    elif cat == 'P':
                        puntajes2.append(40)
            contador = 3
        else:
            contador += 1

    # Completar categorias no usadas con 0
    i = 0
    while i < len(lista_cat):
        ok = False
        j = 0
        while j < len(lista_cat_usados2):
            if lista_cat[i] == lista_cat_usados2[j]:
                ok = True
            j += 1
        if ok == False:
            lista_cat_usados2.append(lista_cat[i])
            puntajes2.append(0)
        i += 1

    print(f'El jugador 2 puntuo {punt2}')
    return terminar


def juego():
    lista_cat_usados1 = []
    puntajes1 = []
    lista_cat_usados2 = []
    puntajes2 = []
    turno = 1
    terminar = False

    while terminar == False:
        if turno % 2 == 0:
            print("Es el turno del jugador 2")
            terminar = jugador2(lista_cat_usados2, puntajes2)
        else:
            print("Es el turno del jugador 1")
            terminar = jugador1(lista_cat_usados1, puntajes1)

        turno += 1

        if turno > 22:
            ganador(puntajes1,puntajes2)
            terminar = True

    

juego()