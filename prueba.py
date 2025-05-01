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

def validar_entero():
    opc_input = input("\nSeleccione una opción: ")
    if opc_input.isdigit():
        return(int(opc_input))
    else:
        return 0

def en_construccion():
    input("En construccion. Presione cualquier tecla para continuar")
    os.system('cls')

def volver():
    input("Regresando al menu anterior. Presione cualquier tecla para continuar")
    os.system('cls')

def menu_report (): #menu 4
    opc = 0
    while opc != 4:
        print("Menú de reportes: \n")
        print("1) Reporte de ventas (confirmadas)")
        print("2) Reporte de vuelos")
        print("3) Reporte de usuarios")
        print("4) Volver")
        opc = validar_entero()
        os.system('cls')
        match opc:
            case 1:
                en_construccion()
            case 2:
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                volver()
            case _:
                print("Opción no válida. Intentelo nuevamente \n")        

def ver_nov():
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

def menu_editar_nov():
        print("Seleccione algun aspecto editable: \n")
        print("1) codigo")
        print("2) descripcion")
        print("3) fecha de inicio")
        print("4) fecha de finalizacion")
        print("5) volver")

def validar_codigo():
    nuevo_codigo = -1
    while nuevo_codigo <0:
        nuevo_codigo = input("Ingrese el nuevo codigo (DEBE SER ENTERO POSITIVO, 0 PARA SALIR)\n")
        if nuevo_codigo.isdigit():
            nuevo_codigo = int(nuevo_codigo)
        else:
            nuevo_codigo = -1
            print("El codigo debe ser un numero entero")
    os.system('cls')
    return nuevo_codigo

def editar_nov(): #menu3_2
    global codigo_nove1, codigo_nove2, codigo_nove3, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_ini_nove2, fecha_fin_nove3
    opc_novedad = 0

    while opc_novedad != 4:
        print("Lista de novedades disponibles:\n")
        print("1) Novedad 1")
        print("2) Novedad 2")
        print("3) Novedad 3")
        print("4) Volver")
        # print("\nSeleccione una novedad para editar: ")
        opc_novedad = validar_entero()
        os.system('cls')
        opc_aspecto = 0
        match opc_novedad:
            case 1:
                while opc_aspecto != 5:
                    menu_editar_nov()
                    opc_aspecto = validar_entero()
                    os.system('cls')    
                    match opc_aspecto:                
                        case 1:
                            print("El codigo actual es:", codigo_nove1)
                            nuevo_codigo = validar_codigo()
                            if nuevo_codigo != 0:
                                codigo_nove1 = nuevo_codigo
                        case 2:
                            print("El texto actual es:", texto_nove1)
                            texto_nove1= input("Ingrese el nuevo texto: ")
                        case 3:
                            print("La fecha actual es:", fecha_ini_nove1)
                            fecha_ini_nove1= input("Ingrese una nueva fecha: ")
                        case 4:
                            print("La fecha actual es:", fecha_fin_nove1)
                            fecha_fin_nove1= input("Ingrese una nueva fecha: ")
                        case 5:
                            volver()
                        case _:
                            print("Opción no válida. Intentelo nuevamente")
                    print("")
            case 2:
                while opc_aspecto != 5:
                    menu_editar_nov()
                    opc_aspecto = validar_entero()
                    os.system('cls')
                    match opc_aspecto:
                        case 1:
                            print("El codigo actual es:", codigo_nove2)
                            nuevo_codigo = validar_codigo()
                            if nuevo_codigo != 0:
                                codigo_nove2 = nuevo_codigo
                        case 2:
                            print("El texto actual es:", texto_nove2)
                            texto_nove2= input("Ingrese el nuevo texto: ")
                        case 3:
                            print("La fecha actual es:", fecha_ini_nove2)
                            fecha_ini_nove2= input("Ingrese una nueva fecha: ")
                        case 4:
                            print("La fecha actual es:", fecha_fin_nove2)
                            fecha_fin_nove2= input("Ingrese una nueva fecha: ")
                        case 5:
                            volver()
                        case _:
                            print("Opción no válida. Intentelo nuevamente")
                    print("")
            case 3:
                while opc_aspecto != 5:
                    menu_editar_nov()
                    opc_aspecto = validar_entero()
                    os.system('cls')
                    match opc_aspecto:
                        case 1:
                            print("El codigo actual es:", codigo_nove3)
                            nuevo_codigo = validar_codigo()
                            if nuevo_codigo != 0:
                                codigo_nove3 = nuevo_codigo
                        case 2:
                            print("El texto actual es:", texto_nove3)
                            texto_nove3= input("Ingrese el nuevo texto: ")
                        case 3:
                            print("La fecha actual es:", fecha_ini_nove3)
                            fecha_ini_nove3= input("Ingrese una nueva fecha: ")
                        case 4:
                            print("La fecha actual es:", fecha_fin_nove3)
                            fecha_fin_nove3= input("Ingrese una nueva fecha: ")
                        case 5:
                            volver()
                        case _:
                            print("Opción no válida. Intentelo nuevamente")
                    print("")
            case 4:
                volver()
            case _:
                print("Opción no válida. Intentelo nuevamente\n")
    os.system('cls')

def menu_novedades(): #menu3
    opc = 0
    while opc != 5:
        print("Menú de novedades: \n")
        print("1) Crear novedades")
        print("2) Modificar novedades")
        print("3) Eliminar novedades")
        print("4) Ver novedades")
        print("5) Volver")
        opc = validar_entero()
        os.system('cls')
        match opc:
            case 1:
                en_construccion()
            case 2:
                editar_nov()
            case 3:
                en_construccion()
            case 4:
                ver_nov()
            case 5:
                volver()
            case _:
                print("Opción no válida. Intentelo nuevamente \n")
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
                codigo_IATA = input("\nIngrese el codigo IATA\n")
                if codigo_IATA.isdigit():
                    codigo_IATA = int(codigo_IATA)
                    if codigo_IATA > 999 or codigo_IATA < 1:
                        print("\nEl codigo debe ser de un maximo de 3 digitos y mayor a 0. Intentelo nuevamente.")
                else:
                    print("\nEl codigo debe ser un numero entero. Intentelo nuevamente.")
                    codigo_IATA = 0
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
    volver()

def menu_gestion_aereo(): #menu 1
    opc = 0
    while opc != 4:
        print("Menú de gestion de aerolineas: \n")
        print("1) Crear aereolineas")
        print("2) Modificar aereolinea")
        print("3) Eliminar Aerolinea")
        print("4) Volver")
        opc = validar_entero()
        os.system('cls')
        match opc:
            case 1:
                crear_aereo()
            case 2:
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                volver()
            case _:
                print("Opción no válida. Intentelo nuevamente \n")

def menu_principal():
    opc = 0
    while opc != 5:
        print("Menú principal: \n")
        print("1) Gestion de aerolineas")
        print("2) Aprobar/Denegar promos")
        print("3) Gestion de novedades")
        print("4) Mostrar reportes")
        print("5) Salir")
        opc = validar_entero()
        
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
                os.system('cls')
            case _:
                print("Opción no válida. Intentelo nuevamente \n")

while intentos != 0:
    usuario = (input("Ingrese su usuario: "))
    contraseña = getpass("Ingrese su contraseña: ")
    os.system('cls')
    if usuario == usu_admin and contraseña == contraseña_admin: 
            intentos = 0
            menu_principal()
    else:
            intentos = intentos - 1
            if intentos == 0: 
                print("\nHubieron 3 intentos fallidos. Por medidas de seguridad se cerrara el programa\n")
            else:
                print ("\nContraseña o usuario incorrectas, le quedan", intentos,"intentos\n" )
print("Se ha cerrado el programa")