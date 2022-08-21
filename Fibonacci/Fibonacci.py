
def main():
    lista = [0, 1]
    n = input("Cuantos numeros quieres sumar: ")
    for i in range(3, int(n)):
        lista.append(lista[len(lista)-1] + lista[len(lista)-2])
    print(lista)


if __name__ == "__main__":
    main()
