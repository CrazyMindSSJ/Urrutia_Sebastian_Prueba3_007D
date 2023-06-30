import numpy
import time
import os
import msvcrt

hotel=numpy.zeros((2,5),int)

lista_ruts=[]
lista_nombres=[]
lista_id_mascotas=[]
lista_nombres_mascotas=[]
lista_filas=[]
lista_columnas=[]
lista_dias=[]

acum=0

def mostrar_menu():
    print("""Menú
    1. Grabar
    2. Buscar
    3. Retirarse y pagar
    4. Salir""")

def validar_opcion():
    while True:
        try:
            opcion=int(input("Ingrese la opción: "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! DEBE INGRESAR UNA OPCIÓN VALIDA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su Rut(Sin puntos ni digito verificador): "))
            if rut>=1000000 and rut<=99999999:
                return rut
            else:
                print("ERROR! DEBE INGRESAR UN RUT VALIDO ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre=input("Ingrese su nombre: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE VALIDO!")

def id_mascota(acum):
    acum=acum+1
    return acum

def validar_nombre_mascota():
    while True:
        nombre=input("Ingrese nombre de la mascota: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE VALIDO!")

def validar_cantidad_dias():
    while True:
        try:
            cantidad=int(input("Ingrese cantidad de dias(entre 1 y 30): "))
            if cantidad>=1 and cantidad<=30:
                return cantidad
            else:
                print("ERROR! DEBE INGRESAR UNA CANTIDAD ENTRE 1 y 30!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")



def habitaciones():
    for x in range(2):
        print("Piso", x+1,':',end=' ')
        for y in range(5):
            print(hotel[x][y],end=' ')
        print()
    print('Piezas:  1 2 3 4 5')

def validar_piso():
    while True:
        try:
            piso=int(input('Ingrese piso de pieza(1 o 2): '))
            if piso in (1,2):
                return piso
            else:
                print("ERROR! Ingrese un piso entre 1 o 2!")
        except:
            print("ERROR! Ingrese un número entero")

def validar_pieza():
    while True:
        try:
            pieza=int(input('Ingrese pieza(1,2,3,4,5): '))
            if pieza in (1,2,3,4,5):
                return pieza
            else:
                print("ERROR! Ingrese una pieza entre 1 y 5!")
        except:
            print("ERROR! Ingrese un número entero")


def reservar():
    piso=validar_piso()
    pieza=validar_pieza()
    if piso in hotel[piso-1]==1 and pieza in hotel[pieza-1]==1:
        print("HABITACION NO DISPONIBLE!")
    else:
        hotel[piso-1][pieza-1]=1
        lista_filas.append(piso)
        lista_columnas.append(pieza)
        return hotel
     
def grabar():
    rut=validar_rut()
    nombre=validar_nombre()
    mascota=id_mascota(acum)
    nombre_mascota=validar_nombre_mascota()
    if 0 not in hotel:
        print("SIN PIEZAS DISPONIBLES!")
        return
    habitaciones()
    dias=validar_cantidad_dias()
    reserva=reservar()
    lista_ruts.append(rut)
    lista_nombres.append(nombre)
    lista_id_mascotas.append(mascota)
    lista_nombres_mascotas.append(nombre_mascota)
    lista_dias.append(dias)
    print("Presione tecla para continuar...")
    msvcrt.getch()

def buscar_rut(rut):
    for x in range(len(lista_ruts)):
            if rut==lista_ruts[x]:
                posicion_encontrada=x
    print('Rut dueño:',lista_ruts[posicion_encontrada])
    print('Nombre dueño:',lista_nombres[posicion_encontrada])
    print('Nombre mascota:',lista_nombres_mascotas[posicion_encontrada])
    print('Id de mascota:',lista_id_mascotas[posicion_encontrada])
    print('Piso:',lista_filas[posicion_encontrada])
    print('Pieza:',lista_columnas[posicion_encontrada])
    print("Presione tecla para continuar...")
    msvcrt.getch()
    return

def buscar():
    rut=validar_rut()
    if rut in lista_ruts:
        buscar_rut(rut)
    else:
        print("ERROR! RUT NO REGISTRADO!")

def retirarse():
    rut=validar_rut()
    if rut in lista_ruts:
        for x in range(len(lista_ruts)):
            if rut==lista_ruts[x]:
                posicion_encontrada=x
        cantidad=lista_dias[posicion_encontrada]
        total=cantidad*15000
        print("Su total a pagar es de: $",total)
    else:
        print("ERROR! Rut ingresado no esta registrado")

def salir():
    print("Gracias por preferirnos, adios!")