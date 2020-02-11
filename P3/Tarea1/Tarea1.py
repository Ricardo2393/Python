
def printr():
    print("\nLista")
    num = 1
    for dict in sm:
        for p,q in dict.items():
            print(str(num) + ". " + p  + " , Cantidad: " + str(q)  )
        num += 1


if __name__ == "__main__":


    print("Lista del Super")
    sm = []
    item = {}

    archivo = open("super.txt", "r")
    for linea in archivo:
        item[linea.rstrip('\n')] = 1
    for a,b in item.items():
        sm.append({a : b})
    print(sm)
    archivo.close()
    

    for n in range(3):
        articulo = input("Articulo: ")
        h = 0
    for p,q in item.items():
            if p.lower() == articulo.lower():
                mas = {p.capitalize() : q+1}
                sm[h].update(mas)
                item.update(mas)
                break
            elif h+1 == len(sm):
                new = {articulo.capitalize() : 1}
                sm.append(new)
                item.update(new)
                break
            h += 1
   

    printr()

    while True:
        try:
            opc = int(input("\nArt. por Eliminar (n): "))
        except:
            print("Numero invalido")
            opc = len(sm)+1
        if opc <= len(sm) and opc > 0:
            break
        else:
            print("Articulo no existe")

    [[key, value]] = sm[opc-1].items()
    print("\nEstariamos eliminando: " + key)
    sm.pop(opc-1)

    printr()

    while True:
        try:
            opc = int(input("\nArt. por Sustituir (n): "))
        except:
            print("Numero invalido")
            opc = len(sm)+1
        if opc <= len(sm) and opc > 0:
            break
        else:
            print("Articulo no existe")

    [[key, value]] = sm[opc-1].items()
    print("\nEstariamos sustituyendo: " + key)
    articulo = input("Nuevo Articulo: ")
    cambio = {articulo.capitalize() : value}
    sm[opc-1] = cambio

    printr()

    archivo = open("super.txt", "a+")
    for a in sm:
        for p,q in a.items():
            archivo.write(p + "\n")
    archivo.close()
