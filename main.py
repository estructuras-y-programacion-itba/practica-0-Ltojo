import random

def tirar(num):
    i = 0
    lista_tirada = [] 
    while i < num:  
        numero = random.randint(1,6)
        lista_tirada.append(numero)
        i += 1
    return lista_tirada

def jugador1():
    lista_cat =[1,2,3,4,5,6,"E","F",'G',"P"]
    lista_cat_usados = []
    puntajes=[]
    terminar = False
    ##lista_conservados=[]
    turno = 1
    while terminar == False:
        if turno % 2 == 0:
            print("es el turno del jugador 2")
            #llamas jugados 2

        else: 
            print("es el turno del jugador 1")
            #llamas jugador1  
        lista_conservados=[]
        contador = 0
        while contador < 3:
            tiradas = tirar((5-len(lista_conservados)))
            print(tiradas)
            
            for elem in tiradas: #preguntamos por todos los elementos
                dec=input('Desea guardar',elem,' ? S/N')
                if dec == "S" or dec== "s":
                    lista_conservados.append(elem)
            
            print(lista_conservados)
            pun = input("desea finalizar: ")
            if pun == "s" or pun =="S":
                cat=input('Ingrese categoria seleciconada:')
                if cat not in lista_cat_usados:
                    lista_cat_usados.append(cat)
                    if 1<=cat<=6:
                        for num in lista_conservados:
                            if num == cat:
                                punt1+=num
                        puntajes.append(punt1)
                    else:
                        if cat=='G':
                            if contador==0:
                                print("gana el jugador1 por generala")
                                terminar=True
                            else:
                                puntajes.append(50)
                        elif cat=='E':
                            puntajes.append(20)
                        elif cat=='F':
                            puntajes.append(30)
                        elif cat=='P':
                            puntajes.append(40)
                contador=3
            else:
                contador += 1
    for i in range(len(lista_cat)):
        ok=False
        for j in range(len(lista_cat_usados)):
            if lista_cat[j]==lista_cat_usados[i]:
                ok=True
        if ok==False:
            lista_cat_usados.append(lista_cat)
            puntajes.append(0)
    return lista_cat_usados, puntajes
        
def jugador2():
    lista_cat =[1,2,3,4,5,6,"E","F",'G',"P"]
    lista_cat_usados = []
    puntajes=[]
    terminar = False
    ##lista_conservados=[]
    turno = 1
    while terminar == False:
        if turno % 2 == 0:
            print("es el turno del jugador 2")
            #llamas jugados 2

        else: 
            print("es el turno del jugador 1")
            #llamas jugador1  
        lista_conservados=[]
        contador = 0
        while contador < 3:
            tiradas = tirar((5-len(lista_conservados)))
            print(tiradas)
            
            for elem in tiradas: #preguntamos por todos los elementos
                dec=input('Desea guardar',elem,' ? S/N')
                if dec == "S" or dec== "s":
                    lista_conservados.append(elem)
            
            print(lista_conservados)
            pun = input("desea finalizar: ")
            if pun == "s" or pun =="S":
                cat=input('Ingrese categoria seleciconada:')
                if cat not in lista_cat_usados:
                    lista_cat_usados.append(cat)
                    if 1<=cat<=6:
                        for num in lista_conservados:
                            if num == cat:
                                punt1+=num
                        puntajes.append(punt1)
                    else:
                        if cat=='G':
                            if contador==0:
                                print("gana el jugador2 por generala")
                                terminar=True
                            else:
                                puntajes.append(50)
                        elif cat=='E':
                            puntajes.append(20)
                        elif cat=='F':
                            puntajes.append(30)
                        elif cat=='P':
                            puntajes.append(40)
                contador=3
            else:
                contador += 1
    for i in range(len(lista_cat)):
        ok=False
        for j in range(len(lista_cat_usados)):
            if lista_cat[j]==lista_cat_usados[i]:
                ok=True
        if ok==False:
            lista_cat_usados.append(lista_cat)
            puntajes.append(0)
    return lista_cat_usados, puntajes

def juego():
    turno = 1
    terminar = False
    while terminar == False:
        if turno % 2 == 0:
            print("es el turno del jugador 2")
            jugador2()

        else: 
            print("es el turno del jugador 1")
            jugador1() 

        turno += 1

        if turno >22:
            terminar = True
            print('hacer')# calculo quien gano por puntos
        