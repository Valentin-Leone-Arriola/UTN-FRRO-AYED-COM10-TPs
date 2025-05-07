import pwinput #es necesario instalacion para que funcione. pip install pwinput en terminal
import os
from datetime import datetime

intentos = 3

usu_admin = "a"
contraseña_admin = "admin"

codigo_nove1 = 121
texto_nove1 = "por aniversario todos los vuelos tiene un %20 de descuento con cualquier medio de pago"
fecha_ini_nove1 = "02/10/2025"
fecha_fin_nove1 = "01/11/2025"
codigo_nove2 = 135
texto_nove2 = "cambio de tarifa referente al equipaje extra en pasajes turista"
fecha_ini_nove2 = "23/06/2025"
fecha_fin_nove2 = "23/07/2025"
codigo_nove3 = 142
texto_nove3 = "los vuelos con destino a Miami seran suspendidos por fuertes tormentas y posibilidad de huracan"
fecha_ini_nove3 = "04/08/2025"
fecha_fin_nove3 = '11/08/2025'

def validar_entero():
    opc_input = input("\nSeleccione una opción valida: ")
    if opc_input.isdigit():
        return(int(opc_input))
    else:
        return -1

def pedir_fecha_valida():
    fecha_valida = False
    while not fecha_valida:
        fecha = input("Ingrese la fecha en formato dd/mm/aaaa")
        try:
            datetime.strptime(fecha,"%d/%m/%Y")
            fecha_valida = True
        except:
            print("Error: Fecha inexistente. Verificá los valores.")
    return fecha

def en_construccion():
    input("En construccion. Presione enter para continuar")
    os.system('cls')

def volver():
    input("Regresando al menu anterior. Presione enter para continuar")
    os.system('cls')

def menu_report (): #menu 4
    opc = -1
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
    print("novedad #", codigo_nove1, "descripcion:", texto_nove1)
    print("con fecha del", fecha_ini_nove1,
          "hasta", fecha_ini_nove1)
    print()
    print("novedad #", codigo_nove2, "descripcion:", texto_nove2)
    print("con fecha del", fecha_ini_nove2,
          "hasta", fecha_fin_nove2)
    print()
    print("novedad #", codigo_nove3, "descripcion:", texto_nove3)
    print("con fecha del", fecha_ini_nove3,
          "hasta", fecha_fin_nove3)
    print()
    input("presione cualquier tecla para continuar")
    os.system('cls')

def validar_codigo():
    nuevo_codigo = -1
    while nuevo_codigo <0:
        nuevo_codigo = input("Ingrese el nuevo codigo (DEBE SER ENTERO POSITIVO, 0 PARA SALIR)\n")
        if nuevo_codigo.isdigit():
            nuevo_codigo = int(nuevo_codigo)
        else:
            nuevo_codigo = -1
            print("El codigo debe ser un numero entero positivo")
    os.system('cls')
    return nuevo_codigo

def menu_editar_nov():
        print("Seleccione algun aspecto editable: \n")
        print("1) codigo")
        print("2) descripcion")
        print("3) fecha de inicio")
        print("4) fecha de finalizacion")
        print("5) volver")

def editar_nov(): #menu3_2
    global codigo_nove1, codigo_nove2, codigo_nove3, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_ini_nove2, fecha_fin_nove3
    
    print("Ingrese el codigo de la novedad (0 para salir)")
    opc_novedad = validar_entero()
    while opc_novedad !=0:
        while opc_novedad != 0 and opc_novedad != codigo_nove1 and opc_novedad != codigo_nove2 and opc_novedad !=codigo_nove3: #se hace con if anidados ya que la consigna dice "el sistema permitirá según el código de novedad ingresado poder editar los datos de la misma."
            print("Opcion invalida. Ingrese el codigo de la novedad (0 para salir)")
            opc_novedad = validar_entero()
        os.system('cls')
        opc_aspecto = -1
        if opc_novedad == codigo_nove1:
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
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") <= datetime.strptime(fecha_fin_nove1,"%d/%m/%Y"):
                            fecha_ini_nove1 = fecha_aux
                        else:
                            print("La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original")
                    case 4:
                        print("La fecha actual es:", fecha_fin_nove1)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") >= datetime.strptime(fecha_ini_nove1,"%d/%m/%Y"):
                            fecha_fin_nove1 = fecha_aux
                        else:
                            print("La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original")
                    case 5:
                        volver()
                    case _:
                        print("Opción no válida. Intentelo nuevamente")
                print("")
        elif opc_novedad == codigo_nove2:
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
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") <= datetime.strptime(fecha_fin_nove2,"%d/%m/%Y"):
                            fecha_ini_nove2 = fecha_aux
                        else:
                            print("La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original")
                    case 4:
                        print("La fecha actual es:", fecha_fin_nove2)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") >= datetime.strptime(fecha_ini_nove2,"%d/%m/%Y"):
                            fecha_fin_nove2 = fecha_aux
                        else:
                            print("La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original")
                    case 5:
                        volver()
                    case _:
                        print("Opción no válida. Intentelo nuevamente")
                print("")
        elif opc_novedad == codigo_nove3:
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
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") <= datetime.strptime(fecha_fin_nove3,"%d/%m/%Y"):
                            fecha_ini_nove3 = fecha_aux
                        else:
                            print("La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original")
                    case 4:
                        print("La fecha actual es:", fecha_fin_nove3)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") >= datetime.strptime(fecha_ini_nove3,"%d/%m/%Y"):
                            fecha_fin_nove3 = fecha_aux
                        else:
                            print("La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original")
                    case 5:
                        volver()
                    case _:
                        print("Opción no válida. Intentelo nuevamente")
                print("")
            print("Ingrese el codigo de la novedad (0 para salir)")
            opc_novedad = validar_entero()
    os.system('cls')
    volver()
    os.system('cls')



def menu_novedades(): #menu3
    opc = -1
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

def crear_aereo():
    nombre_aereo = ""
    contador_arg = 0
    contador_chi = 0
    contador_bra = 0
    while nombre_aereo != 'FIN':
        nombre_aereo = input('Ingrese el nombre del aereo ("FIN" para salir)\n')
        if nombre_aereo != "FIN":
            codigo_IATA = 1000
            while codigo_IATA > 999 or codigo_IATA < 1:
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

def mostrar_menu_gestion_aereo():
        print("╔════════════════════════════════════════╗")
        print("║      MENÚ DE GESTIÓN DE AEROLÍNEAS     ║")
        print("╚════════════════════════════════════════╝\n")
        print("1) Crear Aerolínea")
        print("2) Modificar Aerolínea")
        print("3) Eliminar Aerolínea")
        print("4) Volver al menú principal")

def menu_gestion_aereo(): #menu 1
    opc = -1
    while opc != 4:
        mostrar_menu_gestion_aereo()
        opc = validar_entero()
        os.system('cls')
        while opc <1 or opc >4:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_gestion_aereo()
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

def mostrar_menu_principal():
    print("╔════════════════════════════════════╗")
    print("║        ✈  MENÚ PRINCIPAL  ✈        ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Gestión de Aerolíneas 🛩️")
    print("2) Aprobar / Denegar Promociones💲")
    print("3) Gestión de Novedades 📆")
    print("4) Mostrar Reportes 📊")
    print("5) Salir del Programa ❌")

def menu_principal():
    opc = -1
    while opc != 5:
        mostrar_menu_principal()
        opc = validar_entero()
        os.system('cls')
        while opc < 1 or opc > 5:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_principal()
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
                os.system('cls') #se borra la consola ya que la consigna dice que con salir se abandona el sistema

while intentos != 0:
    usuario = (input("Ingrese su usuario: "))
    contraseña = pwinput.pwinput(prompt="Ingrese la contraseña: ")
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
