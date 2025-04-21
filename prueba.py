from getpass import getpass
import os



def crear_aereo():
    nombre_aereo = ""
    contador_arg = 0
    contador_chi = 0
    contador_bra = 0
    while nombre_aereo != 'FIN':
        nombre_aereo = input('Ingrese el nombre del aereo ("FIN" para salir)\n')
        if nombre_aereo != "FIN":
            codigo_IATA = 1000
            while codigo_IATA > 999 or codigo_IATA < 1:#ES NECESARIO VALIDAR QUE NO SEA NEGATIVO?
                codigo_IATA = int(input("\nIngrese el codigo IATA\n"))
                if codigo_IATA > 999 or codigo_IATA < 1:
                    print("\nEl codigo debe ser de un maximo de 3 digitos y mayor a 0. Intentelo nuevamente.\n")
            descripcion = input("\nIngrese la descripcion del vuelo\n")
            codigo_pais = ""
            while codigo_pais != "ARG" and codigo_pais != "CHI" and codigo_pais != "BRA":
                print("\nCodigo de pais:")
                print('- "ARG"')
                print('- "CHI"')
                print('- "BRA"')
                codigo_pais = input("Ingrese la opcion que desea (SIN ESPACIOS O CARACTERES ESPECIALES Y TODO EN MAYUSCULAS)\n")
                print("")
                match codigo_pais:
                    case "ARG":
                        contador_arg+=1
                    case "CHI":
                        contador_chi+=1
                    case "BRA":
                        contador_bra+=1
                    case _:
                        print("Opcion invalida. Intentelo nuevamente\n")
    
    if contador_arg == contador_chi == contador_bra:
        print("Los tres codigos (ARG, CHI y BRA) tienen la misma cantidad de aerolineas cargadas:", contador_arg)
        print("")
    else:
        mayor = contador_arg
        codigo_mayor = "ARG"
        if contador_chi > mayor:
            mayor = contador_chi
            codigo_mayor = "CHI"
            menor = contador_arg
            codigo_menor = "ARG"
        elif contador_chi == mayor:
            codigo_mayor = "ARG y CHI"
            menor = mayor
        else:
            menor = contador_chi
            codigo_menor = "CHI"

        if contador_bra > mayor:
            mayor = contador_bra
            codigo_mayor = "BRA"
        elif contador_bra == mayor:
            if codigo_mayor == "ARG":
                codigo_mayor = "ARG y BRA"
            else:
                codigo_mayor = "CHI y BRA"
        else:
            if contador_bra < menor:
                menor = contador_bra
                codigo_menor = "BRA"
            elif contador_bra == menor:
                if codigo_menor == "ARG":
                    codigo_menor = "ARG y BRA"
                else:
                    codigo_menor = "CHI y BRA"
        print("")
        print("Mayor/Mayores:", codigo_mayor,"con una cantidad de aerolineas cargadas de", mayor)
        print("Menor/Menores:", codigo_menor, "con una cantidad de aerolineas cargada de", menor)
        print("")


def menu_gestion_aereo(): #menu 1
    opc = 0
    while opc != 4:
        print("Menú de gestion de aerolineas: \n")
        print("1) Crear aereolineas")
        print("2) Modificar aereolinea")
        print("3) Gestion de novedades")
        print("4) Volver")
        opc = int(input("\nSeleccione una opcion: "))
        os.system('cls')
        match opc:
            case 1:
                crear_aereo()
            case 2:
                input("en construcción…")
            case 3:
                input("en construcción…")
            case 4:
                print("Volviendo al menu principal...")
            case _:
                print("Opción no válida. Intentelo nuevamente \n")

def en_construccion():
    input("En construccion. Presione cualquier tecla para continuar")

def menu_principal():
    opc = 0
    while opc != 5:
        os.system('cls')
        print("Menú principal: \n")
        print("1) Gestion de aerolineas")
        print("2) Aprobar/Denegar promos")
        print("3) Gestion de novedades")
        print("4) Reportes")
        print("5) Salir")
        opc = int(input("\nSeleccione una opcion menú: "))
        os.system('cls')
        match opc:
            case 1:
                menu_gestion_aereo()
            case 2:
                en_construccion()
            case 3:
                menu_novedades()
            case 4:
                menu_report()
            case 5:
                print("Saliendo...")
            case _:
                print("Opción no válida... \n")


intentos = 3
usu_admin = "a"
contraseña_admin = "admin"
codigo_nove1 = 121
texto_nove1 = "por aniversario todos los vuelos tiene un %20 de descuento con cualquier medio de pago"
fecha_ini_nove1 = "2/10/2025"
fecha_fin_nove1 = "1/11/2025"
codigo_nove2 = 135
texto_nove2 = "cambio de tarifa referente al equipaje extra en pasajes turista"
fecha_ini_nove2 = "23/6/2025"
fecha_fin_nove2 = "23/7/2025"
codigo_nove3 = 142
texto_nove3 = "los vuelos con destino a Miami seran suspendidos por fuertes tormentas y posibilidad de huracan"
fecha_ini_nove3 = "4/8/2025"
fecha_fin_nove3 = "11/8/2025"

while intentos != 0:
    usuario = (input("Ingrese su usuario: "))
    contraseña = getpass("Ingrese su contraseña: ") 
    if usuario == usu_admin and contraseña == contraseña_admin: 
            intentos = 0
            menu_principal()
    else:
            intentos = intentos - 1
            if intentos == 0: 
                print("Hubieron 3 intentos fallidos. Por medidas de seguridad se cerrara el programa\n")
            else:
                print ("Contraseña o usuario incorrectas, le quedan", intentos,"intentos\n" )