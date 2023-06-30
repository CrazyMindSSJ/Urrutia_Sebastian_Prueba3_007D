import Funciones as f

while True:
    f.mostrar_menu()
    opc=f.validar_opcion()
    if opc==1:
        f.grabar()
    elif opc==2:
        f.buscar()
    elif opc==3:
        f.retirarse()
    else:
        f.salir()
        break