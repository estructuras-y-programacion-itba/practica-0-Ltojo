import random
import csv

def ordenar_custom(lista,l2):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            val_i = str(lista[i])
            val_j = str(lista[j])
            if val_i > val_j:
                lista[i], lista[j] = lista[j], lista[i]
                l2[i], l2[j] = l2[j], l2[i]
    return lista, l2

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

def jugador(lista_cat_usados1, puntajes1):
    terminar = False
    lista_conservados = []
    contador = 0
    puntos_ganados_este_turno = 0
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
                pun = input("Desea finalizar: S/N ")
            if pun == "s" or pun == "S":
                cat = input('Ingrese categoria seleccionada: ').upper()
                cat2= input('Ingrese categoria a tachar, Enter para ignorar ').upper()
                if cat not in lista_cat_usados1:
                    lista_cat_usados1.append(cat)
                    if cat.isdigit():
                        cat_num = int(cat)
                        puntos_ganados_este_turno = lista_conservados.count(cat_num) * cat_num
                    else:
                        if cat == 'G':
                            if contador == 0:
                                print("Generala en primer turno")
                                puntos_ganados_este_turno = 80
                                terminar  = True
                            else:
                                puntos_ganados_este_turno = 50
                        elif cat == 'E': 
                            if contador == 0: 
                                puntos_ganados_este_turno = 25 
                            else:
                                puntos_ganados_este_turno = 20
                        elif cat == 'F': 
                            if contador == 0: 
                                puntos_ganados_este_turno = 35 
                            else:
                                puntos_ganados_este_turno = 30
                        elif cat == 'P':                             
                            if contador == 0: 
                                puntos_ganados_este_turno = 45 
                            else:
                                puntos_ganados_este_turno = 40
                    puntajes1.append(puntos_ganados_este_turno)
                if cat2:
                    lista_cat_usados1.append(cat2)
                    puntajes1.append(0)
                finalizar_turno = True
        contador += 1
    lista_cat_usados1,puntajes1=ordenar_custom(lista_cat_usados1,puntajes1)
    print(f'El jugador puntuo {puntos_ganados_este_turno}')
    return lista_cat_usados1, puntajes1, terminar

def buscar_puntaje(categoria_buscada, categorias_jugador, puntajes_jugador):
    for i in range(len(categorias_jugador)):
        if categorias_jugador[i] == categoria_buscada:
            return puntajes_jugador[i] # Si la encuentra, devuelve los puntos
    return "" # Si el bucle termina y no la encontró, devuelve vacío

def abrir_csv(categorias,cat1,puntajes1, cat2, puntajes2):
    try:
        with open('partida_generala.csv', 'w', newline='', encoding='utf-8') as arch:
            escritor=csv.writer(arch)
            escritor.writerow(['categoria', 'j1','j2'])
            for cate in categorias:
                p1=buscar_puntaje(cate,cat1,puntajes1)
                p2=buscar_puntaje(cate,cat2,puntajes2)
                escritor.writerow([cate,p1,p2])
    except FileNotFoundError:
        print('Archivo no encontrado')

def juego():
    todas_cats = ['1', '2', '3', '4', '5', '6', "E", "F", 'G', "P"]
    lista_cat_usados1 = []
    puntajes1 = []
    lista_cat_usados2 = []
    puntajes2 = []
    turno = 1
    terminar = False
    while terminar == False:
        if turno % 2 == 0:
            print("Es el turno del jugador 2")
            lista_cat_usados2, puntajes2,t2 = jugador(lista_cat_usados2, puntajes2)
            if t2:
                print("Ha ganado j2 por Generala Real")
                terminar = True
        else:
            print("Es el turno del jugador 1")
            lista_cat_usados1, puntajes1,t1 = jugador(lista_cat_usados1, puntajes1)
            if t1:
                print("Ha ganado j1 por Generala Real")
                terminar = True
        turno += 1
        if turno > 22:
            ganador(puntajes1,puntajes2)
            terminar = True
        abrir_csv(todas_cats,lista_cat_usados1, puntajes1, lista_cat_usados2, puntajes2)


juego()