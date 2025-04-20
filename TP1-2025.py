#

from getpass import getpass
import os

intentos = 3

usu_admin = "admin@ventaspasajes777.com"
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

def Editar_nov(): #menu3_2 
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
            print("seleccione algun aspecto editable: \n")
            print("1) codigo")
            print("2) descripcion")
            print("3) fecha de inicio")
            print("4) fecha de finalizacion")
            print("5) volver")
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
                print("seleccione algun aspecto editable: \n")
                print("1) codigo")
                print("2) descripcion")
                print("3) fecha de inicio")
                print("4) fecha de finalizacion")
                print("5) volver")
                menu3_2_1 = int(input("seleccione una opcion "))
            os.system('cls')
        elif menu3_2 == 2:
            os.system('cls')
            print("seleccione algun aspecto editable: \n")
            print("1) codigo")
            print("2) descripcion")
            print("3) fecha de inicio")
            print("4) fecha de finalizacion")
            print("5) volver")
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
                print("seleccione algun aspecto editable: \n")
                print("1) codigo")
                print("2) descripcion")
                print("3) fecha de inicio")
                print("4) fecha de finalizacion")
                print("5) volver")
                menu3_2_2 = int(input("seleccione una opcion "))
            os.system('cls')
            
        elif menu3_2 == 3:
            os.system('cls')
            os.system('cls')
            print("seleccione algun aspecto editable: \n")
            print("1) codigo")
            print("2) descripcion")
            print("3) fecha de inicio")
            print("4) fecha de finalizacion")
            print("5) volver")
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
                print("seleccione algun aspecto editable: \n")
                print("1) codigo")
                print("2) descripcion")
                print("3) fecha de inicio")
                print("4) fecha de finalizacion")
                print("5) volver")
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
    input("precione cualquier tecla para continuar")
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

def crear_aereo(): # por terminar
    print("")

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

def menu_principal():
    print("Menú principal: \n")
    print("1) Gestion de aerolineas")
    print("2) Aprobar/Denergar promos")
    print("3) Gestion de novedades")
    print("4) Reportes")
    print("5) Salir")
    menu = int(input("\nSeleccione un menú: "))
    while menu != 5:
        if menu == 1:
            os.system('cls')
            Menu_gestion_aereo()
        elif menu == 2:
            os.system('cls')
            print("en construccion...")
        elif menu == 3:
            os.system('cls')
            Menu_novedades()
        elif menu == 4:
            os.system('cls')
            Menu_report()
        else:
            os.system('cls')
            print("Opción no válida... \n")
        print("Menú principal: \n")
        print("1) Gestion de aerolineas")
        print("2) Aprobar/Denergar promos")
        print("3) Gestion de novedades")
        print("4) Reportes")
        print("5) Salir")
        menu = int(input("\nSeleccione un menú: "))
    os.system('cls')

while intentos != 0:
        usuario = (input("Ingrese su usuario: ")) 
        if usuario == usu_admin:
            contraseña = getpass("Ingrese su contraseña:") 
            if contraseña == contraseña_admin: 
                os.system('cls')
                menu_principal()
            else:
                print ("Contraseña incorrecta... le quedan", intentos-1,"intentos" )  
                intentos = intentos - 1 
                if intentos == 0: 
                    print("Demasiados intentos fallidos.")
print("\nSaliendo...")