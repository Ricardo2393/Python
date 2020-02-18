def pregunta():
    print ("Que quires hacer: ")

def valor_invalido():
    print("valor invalido ingrese otro valor que este entre 1 @ 3")

def menu():

	
	print ("Selecciona una opción")

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
        print ("con esta solo matas a una")
        kill =+1
        ctotal = ctotal - kill
        print("cuantas quedan")
        print(ctotal)
    elif opc ==2:
        print ("con esta solo matas a 5")
        kill =+5
        ctotal = ctotal - kill
        print("cuantas quedan")
        print(ctotal)
    elif opc ==3:
        print ("salieron 3 mas ")
        ctotal = ctotal +3
        print("cuantas quedan")
        print(ctotal)
    elif opc ==9:
        break
    
    
print("cuantas quedan")
print(ctotal)