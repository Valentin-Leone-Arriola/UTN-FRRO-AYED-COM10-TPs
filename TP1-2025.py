#

from getpass import getpass
import os

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

def menu_editar_nov():
        print("NO QUITAR seleccione algun aspecto editable: \n")
        print("1) codigo")
        print("2) descripcion")
        print("3) fecha de inicio")
        print("4) fecha de finalizacion")
        print("5) volver")

def editar_nov(): #menu3_2 
    global codigo_nove1, codigo_nove2, codigo_nove3, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_ini_nove2, fecha_fin_nove3
    print("seleccione una novedad para editar: \n")
    print("1) Novedad 1")
    print("2) Novedad 2")
    print("3) Novedad 3")
    print("4) volver")
    menu3_2 = int(input("\nSeleccione una opcion: "))
    while menu3_2 != 4:
        if menu3_2 == 1:
            os.system('cls')
            menu_editar_nov()
            menu3_2_1 = int(input("seleccione una opcion: "))
            while menu3_2_1 != 5:
                if menu3_2_1 == 1:
                    os.system('cls')
                    print("el codigo actual es:", codigo_nove1)
                    codigo_nove1= int(input("ingrese el nuevo codigo: "))
                elif menu3_2_1 == 2:
                    os.system('cls')
                    print("el texto actual es:", texto_nove1)
                    texto_nove1= str(input("ingrese el nuevo texto: "))
                elif menu3_2_1 == 3:
                    os.system('cls')
                    print("la fecha actual es:", fecha_ini_nove1)
                    fecha_ini_nove1= str(input("ingrese una nueva fecha: "))
                elif menu3_2_1 == 4:
                    os.system('cls')
                    print("la fecha actual es:", fecha_fin_nove1)
                    fecha_fin_nove2= str(input("ingrese una nueva fecha: "))
                else:
                    os.system('cls')
                    print("Opción no válida... \n")
                menu_editar_nov()
                menu3_2_1 = int(input("seleccione una opcion "))
            os.system('cls')
        elif menu3_2 == 2:
            os.system('cls')
            menu_editar_nov()
            menu3_2_2 = int(input("seleccione una opcion: "))
            while menu3_2_2 != 5:
                if menu3_2_2 == 1:
                    os.system('cls')
                    print("el codigo actual es:", codigo_nove2)
                    codigo_nove2= int(input("ingrese el nuevo codigo: "))
                elif menu3_2_2 == 2:
                    os.system('cls')
                    print("el texto actual es:", texto_nove2)
                    texto_nove2= str(input("ingrese el nuevo texto: "))
                elif menu3_2_2 == 3:
                    os.system('cls')
                    print("la fecha actual es:", fecha_ini_nove2)
                    fecha_ini_nove2= str(input("ingrese una nueva fecha: "))
                elif menu3_2_2 == 4:
                    os.system('cls')
                    print("la fecha actual es:", fecha_fin_nove2)
                    fecha_fin_nove2= str(input("ingrese una nueva fecha: "))
                else:
                    os.system('cls')
                    print("Opción no válida... \n")
                menu_editar_nov()
                menu3_2_2 = int(input("seleccione una opcion "))
            os.system('cls')
            
        elif menu3_2 == 3:
            os.system('cls')
            os.system('cls')
            menu_editar_nov()
            menu3_2_3 = int(input("seleccione una opcion: "))
            while menu3_2_3 != 5:
                if menu3_2_3 == 1:
                    os.system('cls')
                    print("el codigo actual es:", codigo_nove3)
                    codigo_nove3= int(input("ingrese el nuevo codigo: "))
                elif menu3_2_3 == 2:
                    os.system('cls')
                    print("el texto actual es:", texto_nove3)
                    texto_nove3= str(input("ingrese el nuevo texto: "))
                elif menu3_2_3 == 3:
                    os.system('cls')
                    print("la fecha actual es:", fecha_ini_nove3)
                    fecha_ini_nove3= str(input("ingrese una nueva fecha: "))
                elif menu3_2_3 == 4:
                    os.system('cls')
                    print("la fecha actual es:", fecha_fin_nove3)
                    fecha_fin_nove3= str(input("ingrese una nueva fecha: "))
                else:
                    os.system('cls')
                    print("Opción no válida... \n")
                menu_editar_nov()
                menu3_2_3 = int(input("seleccione una opcion "))
            os.system('cls')
        else:
            os.system('cls')
            print("Opción no válida... \n")
        print("seleccione una novedad para editar: \n")
        print("1) Novedad 1")
        print("2) Novedad 2")
        print("3) Novedad 3")
        print("4) volver")
        menu3_2 = int(input("\nSeleccione una opcion: "))
    os.system('cls')


#VER CASE EN VEZ DE IF ANIDADO Y QUITAR REDUNDANCIA DE PRINT (HACER COMO EN MENU PRINCIPAL)

def Ver_nov():
    print("novedades disponibles: \n")
    print("novedad #",codigo_nove1, "descripcion:", texto_nove1 )
    print("con fecha del", fecha_ini_nove1 ,"hasta", fecha_fin_nove1)
    print()
    print("novedad #",codigo_nove2, "descripcion:", texto_nove2 )
    print("con fecha del", fecha_ini_nove2 ,"hasta", fecha_fin_nove2)
    print()
    print("novedad #",codigo_nove3, "descripcion:", texto_nove3 )
    print("con fecha del", fecha_ini_nove3 ,"hasta", fecha_fin_nove3)
    print()
    input("presione cualquier tecla para continuar")
    os.system('cls')

def Menu_novedades(): #menu3
    print("Menú de novedades: \n")
    print("1) Crear novedades")
    print("2) Modificar novedades")
    print("3) Eliminar novedades")
    print("4) Ver novedades")
    print("5) Volver")
    menu3 = int(input("\nSeleccione una opcion: "))
    while menu3 != 5:
        if menu3 == 1:
            os.system('cls')
            print("En construcción…")
        elif menu3 == 2:
            os.system('cls')
            Editar_nov()
        elif menu3 == 3:
            os.system('cls')
            print("En construcción…")
        elif menu3 == 4:
            os.system('cls')
            Ver_nov()
        else:
            os.system('cls')
            print("Opción no válida... \n")
        print("Menú de novedades: \n")
        print("1) Crear novedades")
        print("2) Modificar novedades")
        print("3) Eliminar novedades")
        print("4) Ver novedades")
        print("5) Volver")
        menu3 = int(input("\nSeleccione una opcion: "))
    os.system('cls')


#VER CASE EN VEZ DE IF ANIDADO Y QUITAR REDUNDANCIA DE PRINT (HACER COMO EN MENU PRINCIPAL)

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


def Menu_gestion_aereo(): #menu1
    print("Menú de gestion de aerolineas: \n")
    print("1) Crear aereolineas")
    print("2) Modificar aereolinea")
    print("3) Gestion de novedades")
    print("4) Volver")
    menu1 = int(input("\nSeleccione una opcion: "))
    while menu1 != 4:
        if menu1 == 1:
            os.system('cls')
            crear_aereo()
        elif menu1 == 2:
            os.system('cls')
            print("En construcción…")
        elif menu1 == 3:
            os.system('cls')
            print("En construcción…")
        else:
            os.system('cls')
            print("Opción no válida... \n")
        print("Menú de gestion de aerolineas: \n")
        print("1) Crear aereolineas")
        print("2) Modificar aereolinea")
        print("3) Gestion de novedades")
        print("4) Volver")
        menu1 = int(input("\nSeleccione una opcion: "))
    os.system('cls')

#VER CASE EN VEZ DE IF ANIDADO Y QUITAR REDUNDANCIA DE PRINT (HACER COMO EN MENU PRINCIPAL)

def Menu_report (): #menu 4
    print("Menú de reportes: \n")
    print("1) Reporte de ventas (confirmadas)")
    print("2) Reporte de vuelos")
    print("3) Reporte de usuarios")
    print("4) volver")
    menu4 = int(input("\nSeleccione una opcion: "))
    while menu4 != 4:
        if menu4 == 1:
            os.system('cls')
            print("en construccion...")
        elif menu4 == 2:
            os.system('cls')
            print("en construccion...")
        elif menu4 == 3:
            os.system('cls')
            print("en construccion...")
        else:
            os.system('cls')
            print("Opción no válida... \n")
        print("Menú de reportes: \n")
        print("1) Reporte de ventas (confirmadas)")
        print("2) Reporte de vuelos")
        print("3) Reporte de usuarios")
        print("4) volver")
        menu4 = int(input("\nSeleccione una opcion: "))
    os.system('cls')

#VER CASE EN VEZ DE IF ANIDADO Y QUITAR REDUNDANCIA DE PRINT (HACER COMO EN MENU PRINCIPAL)




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
        if opc == 1:
            Menu_gestion_aereo()
        elif opc == 2:
            print("en construccion...")
        elif opc == 3:
            Menu_novedades()
        elif opc == 4:
            Menu_report()
        elif opc == 5:
            print("Saliendo...")
        else:
            print("Opción no válida... \n")



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