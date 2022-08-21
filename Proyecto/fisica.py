import os

menu_pfisica = """ 
1) Ley de ohm
2) Movimiento rectilineo uniforme
3) Conversiones de grados 
5) Salir del programa\n"""

menu_ohm = """ 
*****LEY DE OHM*****
1) Calcular el voltaje
2) Calcular la corriente
3) Calcular la resistencia
4) Regresar al menu principal\n"""

menu_mru = """ 
*****MOVIMIENTO RECTILINIO UNIFORME*****
1) Calcular la velocidad
2) Calcular la distancia
3) Calcular el tiempo
4) Regresar al menu principal\n"""

menu_grados = """ 
*****CONVERSION DE GRADOS*****
1) Kelvin a Celsius
2) Kelvin a Fahrenheit
3) Fahrenheit de Celsius
4) Fahrenheit de Kelvin
5) Celsius de grados 
6) Celsius de Fahrenheit
7) Regresar al menu principal\n"""

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
                break

            else:
                print("Opcion no valida")
                os.system("pause")
                os.system("cls")
                continue

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

            if opc_mru == 2:
                print("CALCULAR LA VELOCIDAD")
                n1 = float(input("Ingrese el distancia: "))
                n2 = float(input("Ingrese la velocidad: "))
                print("\nRESISTENCIA: " , n1/n2)
                os.system("pause")
                os.system("cls")

            if opc_mru == 3:
                print("CALCULAR LA DISTANCIA")
                n1 = float(input("Ingrese el distancia: "))
                n2 = float(input("Ingrese la velocidad: "))
                print("\nRESISTENCIA: " , n1*n2)
                os.system("pause")
                os.system("cls")

            elif opc_mru == 4:
                    break

            else:
                print("Opcion no valida")
                os.system("pause")
                os.system("cls")
                continue

        
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

    
    
