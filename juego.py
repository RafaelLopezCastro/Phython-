import random
from xml.dom import VALIDATION_ERR

global vidaIa 
global vidaPlayer
global manaIA
global magoSelector
global manaPlayer
global guerreroSelector
global picaroSelector
global turno
global vuelta

class guerrero:
    vida = 1000
    ataque = 200
    hablidad1 = 300
    habilidad2 = 250
    defensa = 500
    ira = 200


class mago:
    vida = 850
    ataque = 150
    hablidad1 = 200
    habilidad2 = 180
    defensa = 100
    mana = 200

class picaro:
    vida = 900
    ataque = 300
    hablidad1 = 350
    habilidad2 = 200
    defensa = 150
    energia = 200

def turnoPlayer():
            global vidaIa
            global vidaPlayer
            global guerreroSelector
            global magoSelector
            global picaroSelector
            global manaPlayer
            eleccion3 = input("Acción del personaje: (1)Atacar, (2)Defender, (3)Habilidad1,(4)Habilidad2 ")

            
            if eleccion3 == "2" :
               
                if magoSelector == True:
                     print("Has Defendido: " , " -" , mago.defensa)
                     
                     print("Vida IA:" , vidaPlayer)
                
                     
           
                if guerreroSelector == True:
                    print("Has Defendido: " , " -" , mago.defensa)
                     
                    print("Vida IA:" , vidaPlayer)
                
                    

           
                if picaroSelector == True:
                    print("Has Defendido: " , " -" , mago.defensa)
                     
                    print("Vida IA:" , vidaPlayer)
                
                    
    
                
                
            if eleccion3 == "3" and manaPlayer > 0:
                if magoSelector == True :
                    manaPlayer = int(mago.mana) 
                    manaPlayer -= 10

                    print("Has usado habilidad1: " , " -" , mago.hablidad1 , " Te queda " , manaPlayer)
                    vidaPlayer -= int(mago.hablidad1)
                    print("Vida IA:" , vidaPlayer)
                
                     
           
                if guerreroSelector == True:
                    manaPlayer = int(guerrero.ira) 
                    manaPlayer -= 20

                    print("Has usado habilidad1: " , " -" , guerrero.hablidad1 , " Te queda " , manaPlayer)
                    vidaPlayer -= int(guerrero.hablidad1)
                    print("Vida IA:" , vidaPlayer)
                
                    

           
                if picaroSelector == True:
                    manaPlayer = int(picaro.energia) 
                    manaPlayer -= 15

                    print("Has usado habilidad1: " , " -" , picaro.hablidad1 , " Te queda " , manaPlayer)
                    vidaPlayer -= int(picaro.hablidad1)
                    print("Vida IA:" , vidaPlayer)
                    
            if eleccion3 == "4" and manaPlayer > 0:
                if magoSelector == True :
                    manaPlayer = int(mago.mana)
                    manaPlayer -= 10

                    print("Has usado habilidad1: " , " -" , mago.habilidad2 , " Te queda " , manaPlayer)
                    vidaPlayer -= int(mago.habilidad2)
                    print("Vida Player:" , vidaPlayer)
                
                     
           
                if guerreroSelector == True:
                    manaPlayer = int(guerrero.ira)
                    manaPlayer -= 30

                    print("Has usado habilidad1: " , " -" , guerrero.habilidad2 , " Te queda " , manaPlayer)
                    vidaPlayer -= int(guerrero.habilidad2)
                    print("Vida Player:" , vidaPlayer)
                
                    

           
                if picaroSelector == True:
                    manaPlayer = int(picaro.energia)
                    manaPlayer -= 10

                    print("Has usado habilidad1: " , " -" , picaro.habilidad2 , " Te queda " , manaPlayer)
                    vidaPlayer -= int(picaro.habilidad2)
                    print("Vida Player:" , vidaPlayer)

            if eleccion3 == "1" :
                if magoSelector == True:
                     print("Has atacado: " , " - " , mago.ataque)
                     vidaIa -= int(mago.ataque)
                     print("Vida IA:" , vidaIa)
                
                     
           
                if guerreroSelector == True:
                     print("Has atacado: " , " - " , guerrero.ataque)
                     vidaIa -= int(guerrero.ataque)
                     print("Vida IA:" , vidaIa)
                
                     

           
                if picaroSelector == True:
                     print("Has atacado: " , " - " , picaro.ataque)
                     vidaIa -= int(picaro.ataque)
                     print("Vida IA:" , vidaIa)
                
                     
           


def turnoIA():
    global manaIA
    global vidaPlayer
    global vidaIa
    accionIA = (random.randint(1,4))
    if accionIA == 2 :
                print("Has Defendido: " , " -" , mago.defensa)
                vidaIa += int(mago.defensa)
                print("Vida IA" , vidaIa)
    if accionIA == "3" and manaIA > 0:
                if magoSelector == True :
                    manaIA = int(mago.mana)
                    manaIA -= 10

                    print("Has usado habilidad1: " , " -" , mago.hablidad1 , " Te queda " ,manaIA)
                    vidaPlayer -= int(mago.hablidad1)
                    print("Vida Player:" , vidaPlayer)
                
                     
           
                if guerreroSelector == True:
                    manaIA = int(guerrero.ira)
                    manaIA -= 30

                    print("Has usado habilidad1: " , " -" , guerrero.hablidad1 , " Te queda " , manaIA)
                    vidaPlayer -= int(guerrero.hablidad1)
                    print("Vida Player:" , vidaPlayer)
                
                    

           
                if picaroSelector == True:
                    manaIA = int(picaro.energia)
                    manaIA -= 5

                    print("Has usado habilidad1: " , " -" , picaro.hablidad1 , " Te queda " , manaIA)
                    vidaPlayer -= int(picaro.hablidad1)
                    print("Vida Player:" , vidaPlayer)
                    
    if accionIA == "4" and manaIA > 0:
                if magoSelector == True :
                    manaIA = int(mago.mana)
                    manaIA -= 10

                    print("Has usado habilidad1: " , " -" , mago.habilidad2 , " Te queda " , manaIA)
                    vidaPlayer -= int(mago.habilidad2)
                    print("Vida Player:" , vidaPlayer)
                
                     
           
                if guerreroSelector == True:
                    manaIA = int(guerrero.ira) 
                    manaIA -= 30

                    print("Has usado habilidad1: " , " -" , guerrero.habilidad2 , " Te queda " , manaIA)
                    vidaPlayer -= int(guerrero.habilidad2)
                    print("Vida Player:" , vidaPlayer)
                
                    

           
                if picaroSelector == True:
                    manaIA = int(picaro.energia)
                    manaIA -= 5

                    print("Has usado habilidad1: " , " -" , picaro.habilidad2 , " Te queda " , manaIA)
                    vidaPlayer -= int(picaro.habilidad2)
                    print("Vida Player:" , vidaPlayer)

    if accionIA == 1 :
               
        print("Has atacado: " , " - " , mago.ataque)
        vidaPlayer -= int(mago.ataque)
        print("Vida Player" , vidaPlayer)
                  
                
                
   
                
                

    if accionIA == 1 :
                if numeroIA == 3:
                     print("Has sido atacado: " , " - " , picaro.ataque)
                     vidaPlayer -= int(picaro.ataque)
                     print("Vida Player:" , vidaPlayer)

vuelta = 0
eleccion = input("Que acción se desea realizar ver o elegir? ")



if eleccion == "ver":
        print("Mago:")
        print ("Vida: ", mago.vida)
        print("Maná: " , mago.mana)
        print("Habilidad 1: Bola de fuego")
        print("Habilidad 2: Rayo hielo")

        print("")

        print("Guerrero:")
        print ("Vida: " , guerrero.vida)
        print("Ira: " , guerrero.ira)
        print("Habilidad 1: Aplastar")
        print("Habilidad 2: Gancho")

        print("")


        print("Pícaro:")
        print ("Vida: " , picaro.vida)
        print("Maná: " , picaro.energia)
        print("Habilidad 1: Kunai")
        print("Habilidad 2: Ballistico")
        

if eleccion == "elegir":
    
            print("Mago, Guerrero, Pícaro")
            eleccion2 = input("Que clase quieres usar? ")
            numeroIA = (random.randint(1,3))
            
            if eleccion2 == "Mago" :
                magoSelector = True
                guerreroSelector = False
                picaroSelector = False
                print("Has seleccionado el mago")
                vidaPlayer = int(mago.vida)
                manaPlayer = int(mago.mana)
                
            if eleccion2 == "Guerrero" :
                guerreroSelector = True
                magoSelector = False
                picaroSelector = False
                print("Has seleccionado el guerrero")
                vidaPlayer = int(guerrero.vida)
                manaPlayer = int(guerrero.ira)

            if eleccion2 == "Picaro" :
                picaroSelector = True
                guerreroSelector = False
                magoSelector = False
                print("Has seleccionado al picaro")
                vidaPlayer = int(picaro.vida)
                manaPlayer = int(picaro.energia)

            if numeroIA == 1 :
                print("IA a seleccionado el mago")
                vidaIa = int(mago.vida)
                manaIA = int(mago.mana)

            if numeroIA == 2 :
                print("IA a seleccionado el guerrero")
                vidaIa = int(guerrero.vida)
                manaIA = int(guerrero.ira)
            
            if numeroIA == 3 :
                print("IA a seleccionado al picaro")
                vidaIa = int(picaro.vida)
                manaIA = int(picaro.energia)

            while (vidaPlayer > 0 or vidaIa > 0):
                turno = 1
                turnoPlayer()
                turno += 1
                turnoIA()
                if vidaPlayer <= 0:
                 print("La IA ha ganado")
                break
                if vidaIa <= 0:
                 print("La Player ha ganado")
                break
            vuelta += 1
            
