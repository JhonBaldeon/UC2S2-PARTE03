import os
#Crear archivo
import sys
import modulo

def leer_archivo(archivo):
    archivo= open(archivo,"rt",encoding="utf8")
    leer_archivo = archivo.read()
    leer_archivo=leer_archivo.split("\n")
    return leer_archivo
 
    
ar_usuario = leer_archivo("login.txt")
ar_clave = leer_archivo("clave.txt")


cont =0

while cont != 2:

    usuario = input("Ingresar Usuario:    ")
    clave = input("Ingresar Clave:      ")
    
    for usuarioItem in ar_usuario:
        if usuario == usuarioItem:
            for clave_Item in ar_clave:
                if clave == clave_Item :
                    print("*********Datos Ingresados Correctamente**********\n")
                    print("Datos Personas\n1.Listar Persona\n2.Agregar Personas\n3.Salir")
                    cont = 2
                else :
                    print("**********Datos Incorrectos**********\n")
                    cont += 1            
        else :
            print("**********Datos Incorrectos**********\n")
            cont += 1
            
            