import os
import math


#MENU PRINCIPAL DE LAS MATERIAS
menu_pmaterias = """ 
****************************
BIENVENIDO AL MENU PRINCIPAL
****************************
1) MATERIA DE MATEMATICAS
2) MATERIA DE FISICA
3) MATERIA DE QUIMICA
4) Salir del programa\n"""



#MENUS Y SUBMENUS DE LA MATERIA DE MATEMATICAS
menu_pmatema = """ 
1) Operaciones basicas 
2) Perimetro de figuras
3) Area de figuras
4) Determinante de un matriz 
5) Regresar al menu principal\n"""

menu_opbasicas = """ 
*****OPERACIONES BASICAS*****
1) Suma de dos numeros
2) Resta de dos numeros
3) Multiplicacion de dos numeros
4) Division de dos numeros
5) Potencia de un numero
6) Regresar al menu de la materia\n"""

menu_pefiguras = """ 
*****PERIMETRO DE FIGURAS*****
1) Perimetro de triangulo
2) Perimetro de cuadrado
3) Perimetro de rectangulo
4) Perimetro de circulo
5) Regresar al menu de la materia\n"""

menu_arfiguras = """ 
*****AREA DE FIGURAS*****
1) Area de triangulo
2) Area de cuadrado
3) Area de rectangulo
4) Area de circulo
5) Regresar al menu de la materia\n"""

menu_matriz = """ 
*****DETERMINANTE DE UNA MATRIZ*****
1) Calcular determinante de una matriz
2) Regresar al menu de la materia\n"""



#MENUS Y SUBMENUS DE LA MATERIA DE FISICA
menu_pfisica = """ 
1) Ley de ohm
2) Movimiento rectilineo uniforme
3) Conversiones de grados 
4) Regresar al menu de la materia\n"""

menu_ohm = """ 
*****LEY DE OHM*****
1) Calcular el voltaje
2) Calcular la corriente
3) Calcular la resistencia
4) Regresar al menu de la materia\n"""

menu_mru = """ 
*****MOVIMIENTO RECTILINIO UNIFORME*****
1) Calcular la velocidad
2) Calcular la distancia
3) Calcular el tiempo
4) Regresar al menu de la materia\n"""

menu_grados = """ 
*****CONVERSION DE GRADOS*****
1) Kelvin a Celsius
2) Kelvin a Fahrenheit
3) Fahrenheit de Celsius
4) Fahrenheit de Kelvin
5) Celsius de grados 
6) Celsius de Fahrenheit
7) Regresar al menu de la materia\n"""



#MENUS Y SUBMENUS DE LA MATERIA DE QUIMICA
menu_pquimica = """ 
1) Agregar elemento de la tabla periodica 
2) Mostrar todos los elementos de la tabla periodica
3) Regresar al menu principal\n"""



while menu_pmaterias:
    print(menu_pmaterias)
    opc = int(input("Seleccione la opcion deseada: "))
    os.system("cls")
    
    if opc == 1:
        while menu_pmatema:
            print("\n**************************************")
            print("BIENVENIDO A LA MATERIA DE MATEMATICAS")
            print("**************************************")
            print(menu_pmatema)
            opc = int(input("Seleccione la opcion deseada: "))
            print("**************************************")

            if opc == 1:
                while opc == 1:
                    os.system("cls")
                    print(menu_opbasicas)
                    opc_opbasicas = int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")
                    if opc_opbasicas == 1:
                        print("\n***SUMA***")
                        n1 = float(input("Ingrese el primer numero a sumar: "))
                        n2 = float(input("Ingrese el segundo numero a sumar: "))
                        print("\nRESULTADO: " , n1+n2)
                        os.system("pause")
                        os.system("cls")
                        
                    elif opc_opbasicas == 2:
                        print("\n***RESTA***")
                        n1 = float(input("Ingrese el primer numero a restar: "))
                        n2 = float(input("Ingrese el segundo numero a restar: "))
                        print("\nRESULTADO:" , n1-n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_opbasicas == 3:
                        print("\n***MULTIPLICACION***")
                        n1 = float(input("Ingrese el primer numero a multiplicar: "))
                        n2 = float(input("Ingrese el segundo numero a multiplicar: "))
                        print("\nRESULTADO: " , n1*n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_opbasicas == 4:
                        print("\n***DIVISION***")
                        n1 = float(input("Ingrese el primer numero a dividir: "))
                        n2 = float(input("Ingrese el segundo numero a dividir: "))
                        print("\nRESULTADO: " , n1/n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_opbasicas == 5:
                        print("\n***POTENCIA***")
                        n1 = float(input("Ingrese la base del numero que se va elevar: "))
                        n2 = float(input("Ingrese la potencia del numero base: "))
                        print(pow("\nRESULTADO: " , n1,n2))
                        os.system("pause")
                        os.system("cls")

                    elif opc_opbasicas == 6:
                        os.system("cls")
                        break

                    else:
                        print("Opcion no valida")
                        os.system("pause")
                        os.system("cls")
                        continue
                else:
                    os.system("cls")
                    break  


            elif opc == 2:
                while opc == 2:
                    os.system("cls")
                    print(menu_pefiguras)
                    opc_pefiguras = int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")
                    if opc_pefiguras == 1:
                        print("\n***PERIMETRO DE TRIANGULO***")
                        n1 = float(input("Ingrese el primer lado del tringulo: "))
                        n2 = float(input("Ingrese el segundo lado del tringulo: "))
                        n3 = float(input("Ingrese el tercer lado del tringulo: "))
                        print("\nRESULTADO: ", n1+n2+n3)
                        os.system("pause")
                        os.system("cls")
                        
                    elif opc_pefiguras == 2:
                        print("\n***PERIMETRO DE CUADRADO***")
                        n1 = float(input("Ingrese el lado de cuadrado: "))
                        print("\nRESULTADO:", n1*n1)
                        os.system("pause")
                        os.system("cls")

                    elif opc_pefiguras == 3:
                        print("\n***PERIMETRO DE RECTANGULO***")
                        n1 = float(input("Ingrese el lado A del triangulo: "))
                        n2 = float(input("Ingrese el lado B del triangulo: "))
                        print("\nRESULTADO: ", ((2*n1)+(2*n1)))
                        os.system("pause")
                        os.system("cls")

                    elif opc_pefiguras == 4:
                        PI = math.pi
                        print("\n***PERIMETRO DE CIRCULO***")
                        n1 = float(input("Ingrese el radio del circulo: "))
                        print("\nRESULTADO: ", PI*(n1*2))
                        os.system("pause")
                        os.system("cls")
                    
                    elif opc_pefiguras == 5:
                        os.system("cls")
                        break

                    else:
                        print("Opcion no valida")
                        os.system("pause")
                        os.system("cls")
                        continue
                else:
                    os.system("cls")
                    break  


            elif opc == 3:
                os.system("cls")
                while opc == 3:
                    print(menu_pefiguras)
                    opc_arfiguras = int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")
                    if opc_arfiguras == 1:
                        print("\n***AREA DE TRIANGULO***")
                        n1 = float(input("Ingrese la base del tringulo: "))
                        n2 = float(input("Ingrese la altura del tringulo: "))
                        print("\nRESULTADO: ", (n1*n2)/2)
                        os.system("pause")
                        os.system("cls")
                        
                    elif opc_arfiguras == 2:
                        print("\n***AREA DE CUADRADO***")
                        n1 = float(input("Ingrese el lado de cuadrado: "))
                        print("\nRESULTADO:", n1*n1)
                        os.system("pause")
                        os.system("cls")

                    elif opc_arfiguras == 3:
                        print("\n***AREA DE RECTANGULO***")
                        n1 = float(input("Ingrese el base: "))
                        n2 = float(input("Ingrese el altura: "))
                        print("\nRESULTADO: ", n1*n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_arfiguras == 4:
                        PI = math.pi
                        print("\n***AREA DE CIRCULO***")
                        n1 = float(input("Ingrese el radio del circulo: "))
                        print("\nRESULTADO: ", PI*(n1*2))
                        os.system("pause")
                        os.system("cls")

                    elif opc_arfiguras == 5:
                        os.system("cls")
                        break

                    else:
                        print("Opcion no valida")
                        os.system("pause")
                        os.system("cls")
                        continue
                else:
                    os.system("cls")
                    break  


            elif opc == 4:
                os.system("cls")
                while opc == 4:
                    print(menu_matriz)
                    opc_matriz = int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")     
                    if opc_matriz == 1:
                        matriz = []

                        def mat(n):
                            for i in range (n):
                                matriz.append([])
                                for j in range (n):
                                    matriz[i].append(0)
                            return matriz

                        def llenar(n):
                            matriz = mat(n)
                            for x in range (n):
                                for y in range (n):
                                    matriz[x][y] = float(input("Valor de [" + str(x) + "][" + str(y) + "] = "))

                        def gauss(n):
                            for z in range (n-1):
                                for x in range(1, n-z):
                                    if (matriz[z][z] != 0 ):
                                        p = matriz[x+z][z] / matriz[z][z]
                                        for y in range (n):
                                            matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                                            
                        def det(n):
                            deter=1
                            for x in range (n):
                                deter=matriz[x][x]*deter
                            print ("\nLa determinante de la matriz es = ", deter)
                            print("\nMatriz resultante:")
                            for i in range (n):
                                print (matriz[i][:])

                        n = int(input ("Tamaño de la matriz : "))
                        llenar(n)
                        gauss(n)
                        det(n)
                        input()
                        os.system("pause")
                        os.system("cls")
                
                    elif opc_matriz == 2:
                        os.system("cls")
                        break

                else:
                    print("Opcion no valida")
                    os.system("pause")
                    os.system("cls")
                    continue
            
            elif opc == 5:
                os.system("cls")
                break
            

    elif opc == 2:
        while menu_pfisica:
            print("\n**************************************")
            print("BIENVENIDO A LA MATERIA DE FISICA")
            print("**************************************")
            print(menu_pfisica)
            opc = int(input("Seleccione la opcion deseada: "))
            print("\n**************************************")

            if opc == 1:
                while opc == 1:
                    os.system("cls")
                    print(menu_ohm)
                    opc_ohm = int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")
                    if opc_ohm == 1:
                        print("INGRESE LOS DATOS PARA CALCULAR EL VOLTAJE")
                        n1 = float(input("Ingrese la corriente: "))
                        n2 = float(input("Ingrese la resistencia: "))
                        print("\nVOLTAJE: " , n1*n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_ohm == 2:
                        print("INGRESE LOS DATOS PARA CALCULAR LA CORRIENTE")
                        n1 = float(input("Ingrese el voltaje: "))
                        n2 = float(input("Ingrese la resistencia: "))
                        print("\nCORRIENTE: " , n1/n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_ohm == 3:
                        print("INGRESE LOS DATOS PARA CALCULAR LA RESISTENCIA")
                        n1 = float(input("Ingrese el voltaje: "))
                        n2 = float(input("Ingrese la corriente: "))
                        print("\nRESISTENCIA: " , n1/n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_ohm == 4:
                        os.system("cls")
                        break

                    else:
                        print("Opcion no valida")
                        os.system("pause")
                        os.system("cls")
                        continue
                else:
                    os.system("cls")
                    break  

            elif opc == 2:
                while opc == 2:
                    os.system("cls")
                    print(menu_mru)
                    opc_mru = int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")
                    
                    if opc_mru == 1:
                        print("CALCULAR EL TIEMPO")
                        n1 = float(input("Ingrese el distancia: "))
                        n2 = float(input("Ingrese la velocidad: "))
                        print("\nRESISTENCIA: " , n1/n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_mru == 2:
                        print("CALCULAR LA VELOCIDAD")
                        n1 = float(input("Ingrese el distancia: "))
                        n2 = float(input("Ingrese la velocidad: "))
                        print("\nRESISTENCIA: " , n1/n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_mru == 3:
                        print("CALCULAR LA DISTANCIA")
                        n1 = float(input("Ingrese el distancia: "))
                        n2 = float(input("Ingrese la velocidad: "))
                        print("\nRESISTENCIA: " , n1*n2)
                        os.system("pause")
                        os.system("cls")

                    elif opc_mru == 4:
                        os.system("cls")
                        break

                    else:
                        print("Opcion no valida")
                        os.system("pause")
                        os.system("cls")
                        continue
                else:
                    os.system("cls")
                    break  
                
            elif opc == 3:
                while opc == 3:
                    os.system("cls")
                    print(menu_grados)
                    opc_gra= int(input("Seleccione la opcion deseada: "))
                    print("\n**************************************")
                    if opc_gra == 1:
                        print("CELCIUS A KELVIN")
                        n1 = float(input("Ingrese los grados celsius: "))
                        print("\nGRADOS KELVIN: ", n1+273.15)
                        os.system("pause")
                        os.system("cls")

                    elif opc_gra == 2:
                        print("CELCIUS A FARENHEIT")
                        n1 = float(input("Ingrese los grados celsius: "))
                        print("\nGRADOS FARENHEIT: " , ((9*n1)/5)+32)
                        os.system("pause")
                        os.system("cls")

                    elif opc_gra == 3:
                        print("FAHRENHEIT A CELCIUS")
                        n1 = float(input("Ingrese los grados fahrenheit: "))
                        print("\nGRADOS CELCIUS: " , ((5*(n1-32))/9))
                        os.system("pause")
                        os.system("cls")

                    elif opc_gra == 4:
                        print("FAHRENHEIT KELVIN")
                        n1 = float(input("Ingrese los grados fahrenheit: "))
                        print("\nGRADOS KELVIN: " , ((5*(n1-32))/9)+273.15)   
                        os.system("pause")
                        os.system("cls") 
                        
                    elif opc_gra == 5:
                        print("KELVIN A CELCIUS")
                        n1 = float(input("Ingrese los grado kelvin: "))
                        print("\nGRADOS CELCIUS: " , n1-273.15)
                        os.system("pause")
                        os.system("cls")

                    elif opc_gra == 6:
                        print("KELVIN A FAHRENHEIT")
                        n1 = float(input("Ingrese los grados kelvin: "))
                        print("\nGRADOS FARENHEIT: " , ((9*(n1-273.15))/5)+32)
                        os.system("pause")
                        os.system("cls")

                    elif opc_gra == 7:
                        os.system("cls")
                        break

                    else:
                        print("Opcion no valida")
                        os.system("pause")
                        os.system("cls")
                        continue
                else:
                    os.system("cls")
                    break  
                    
            elif opc == 4:
                os.system("cls")
                break

    elif opc == 3:
        elementos = []

        while menu_pquimica:
            os.system("cls")
            print("\n**************************************")
            print("BIENVENIDO A LA MATERIA DE QUIMICA")
            print("**************************************")
            print(menu_pquimica)
            opc_quimica = int(input("Seleccione la opcion deseada: "))
            print("\n**************************************")
            
            if opc_quimica  == 1:
                num_atomico = input("Ingrese el numero atomico: ")
                sim_quimico = input("Ingrese el simbolo quimico: ")
                nom_elemento = input("Ingrese el nombre de el elemento: ")
                elementos.append([num_atomico.ljust(12), sim_quimico.ljust(14), nom_elemento.ljust(20)])
                os.system("cls")

            elif opc_quimica  == 2:
                print("NUMERO ATOMICO | SIMBOLO QUIMICO | NOMBRE DEL ELEMENTO")      
                for i in range(len(elementos)):
                    print(elementos[i])
                os.system("pause")
                os.system("cls")

            elif opc_quimica  == 3:
                os.system("cls")
                break

            else:
                print("Opcion no valida")
                os.system("pause")
                os.system("cls")
                continue

    else:
        os.system("cls")
        input("\n\nGRACIAS POR USAR ESTE PROGRAMA")
        break  