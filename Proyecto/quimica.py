import os


menu_pquimica = """ 
1) Agregar elemento de la tabla periodica 
2) Mostrar todos los elementos de la tabla periodica
3) Salir del programa\n"""

elementos = []

while menu_pquimica:
    
    print("\n**************************************")
    print("BIENVENIDO A LA MATERIA DE QUIMICA")
    print("**************************************")
    print(menu_pquimica)
    opc_quimica  = int(input("Seleccione la opcion deseada: "))
    print("\n**************************************")
    
    if opc_quimica  == 1:
        num_atomico = input("Ingrese el numero atomico: ")
        sim_quimico = input("Ingrese el simbolo quimico: ")
        nom_elemento = input("Ingrese el nombre de el elemento: ")
        elementos.append([num_atomico.ljust(12), sim_quimico.ljust(14), nom_elemento.ljust(20)])

    elif opc_quimica  == 2:
        print("NUMERO ATOMICO | SIMBOLO QUIMICO | NOMBRE DEL ELEMENTO")      
        for i in range(len(elementos)):
            print(elementos[i])

    elif opc_quimica  == 3:
        break
