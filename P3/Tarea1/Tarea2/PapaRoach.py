def pregunta():
    print ("Que quires hacer: ")

def valor_invalido():
    print("valor invalido ingrese otro valor que este entre 1 @ 3")

def menu():

	
	print ("Selecciona una opción")

	print ("\t1. pisar")

	print ("\t2. fumigar")

	print ("\t3. reproducir")

    
while True:
    ctotal = 10
    kill = 0
    
    
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
    elif opc ==2:
        print ("con esta solo matas a 5")
        kill =+5
    elif opc ==3:
        print ("salieron 3 mas ")
        ctotal = ctotal +3
    break
    
remain = ctotal - kill
print("cuantas quedan")
print(remain)

