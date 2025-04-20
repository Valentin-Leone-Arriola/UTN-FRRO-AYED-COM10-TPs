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


if __name__ == "__main__":
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