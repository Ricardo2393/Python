class Cucaracha:
    def __init__(self, especie, subfilo, name, sci_name):
        self.especie = "insecto"
        self.subfilo = "invertebrado"
        self.name = "Cucaracha"
        self.sci_name = "Blatta"

    def lore(self):
        print("Vez una " + self.name + " que es " + self.especie + " " + self.subfilo)
c1 = Cucaracha("Bicho", "sin wezo", "Cucaracha", "Blatta")

c1.lore()

print("y Hay 10 !!!")





def pregunta():
    print ("\nQue quires hacer: ")

def valor_invalido():
    print("valor invalido ingrese otro valor que este entre 1 @ 3 o 9")

def menu():

	
	print ("\nSelecciona una opción")

	print ("\t1. pisar")

	print ("\t2. fumigar")

	print ("\t3. reproducir")

	print ("\t9. Salir")


 

ctotal = 10
kill = 0   
while True:
    
    
    
    menu()
    
    try:
        pregunta()
        opc = int(input(">>>>>>>>>:"))
    except:
        valor_invalido()
        opc = int(input(">>>>>>>>>:"))

    if opc ==1:
        print ("\ncon esta solo matas a una")
        kill =+1
        ctotal = ctotal - kill
        print("cuantas quedan")
        print("\t: " + str(ctotal))
    elif opc ==2:
        print ("\ncon esta solo matas a 5")
        kill =+5
        ctotal = ctotal - kill
        print("cuantas quedan")
        print("\t: " + str(ctotal))
    elif opc ==3:
        print ("\nsalieron 3 mas ")
        ctotal = ctotal +3
        print("cuantas quedan")
        print("\t: " + str(ctotal))
    elif opc ==9:
        break





