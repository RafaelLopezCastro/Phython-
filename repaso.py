import random

palabraElejida = " "
palabraOculta = []
longitud = 0
intento = 0
palabraElejidaArray = []
lista = []
palabraGanadora = []
palabra1 = "Jugador"
palabra2 = "Mando"
palabra3 = "Juego"
palabra4 = "Carroceria"
palabra5 = "Coche"
palabra6 = "Cualta"
intento = 0
booleana = False
cuerpo1 = ""
cuerpo2 = ""
cuerpo3 = ""
cuerpo4 = ""
cuerpo5 = ""
cuerpo6 = ""

aleatoria = (random.randint(1,6))

    
def muneco():
     global cuerpo1 
     global cuerpo2 
     global cuerpo3 
     global cuerpo4 
     global cuerpo5 
     global cuerpo6 
     global intento
     
     if intento == 1:
            print("   ()")
            
     if intento == 2:
            cuerpo1 = "/-"
            print("   ()")
            print("   ()")
            
     if intento == 3:
            cuerpo2 = "()"
            print("   ()")
            print(cuerpo1 , cuerpo2)
            
     if intento == 4:
            cuerpo3 = "-\\"
            print("   ()")
            print(cuerpo1 , cuerpo2 ,cuerpo3)
     if intento == 5:
         print("   ()")
         print(cuerpo1 , cuerpo2 ,cuerpo3)
         cuerpo4 = " /"
         print("" , cuerpo4)
           
     if intento == 6:
            cuerpo5 = " \\"
            print("   ()")
            print(cuerpo1 , cuerpo2 ,cuerpo3)
            print("",cuerpo4, cuerpo5)
            


   


if aleatoria == 1:
    palabraElejida = palabra1
if aleatoria == 2:
    palabraElejida = palabra2
if aleatoria == 3:
    palabraElejida = palabra3
if aleatoria == 4:
    palabraElejida = palabra4
if aleatoria == 5:
    palabraElejida = palabra5
if aleatoria == 6:
    palabraElejida = palabra6

longitud = 0

for i in palabraElejida:
        lista.append(i)
        palabraOculta.append("_")
print(palabraOculta) 


while intento < 6:
    palabraJugador = input("Introduce la palabra o letra: ")
    intento += 1
    print(intento)

    
    for i in palabraJugador:
        lista.append(i)
    
    for l in palabraElejida:
        palabraElejidaArray.append(l)
        
    if palabraElejida == palabraJugador:
        print("Has ganado")
        booleana = True
        break
        

    for k in range(len(lista)-1):
         
        for w in range(len(palabraElejidaArray)-1):
            if lista[k] == palabraElejidaArray[w]:
                palabraGanadora.append(palabraElejidaArray[k])
        else :
                palabraGanadora.append(" ") 
                muneco()
                booleana = False
                break
            
if booleana != True:
  print("Has perdido")