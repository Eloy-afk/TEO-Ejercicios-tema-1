def lee_numeros(n):
    resultado=[]
    for i in range(n):
        numeros=int(input(f"Introduzca el número {i+1}: "))
        resultado.append(numeros)
    return resultado

if __name__=="__main__":
    n=int(input(f"Introduzca el número de elementos que quiere en la lista: "))
    lista=lee_numeros(n)
    print(lista)
    num_max=max(lista)
    print(f"El número más grande es: {num_max}")
    media=sum(lista)/len(lista)
    print(f"La media de los números que agregó es: {media}")
    pares=0
    for numero in lista:
        if numero%2 == 0:
            pares+=1
    print(f"Cantidad de números pares: {pares}")
    mayores_a_10=[]
    for numero in lista:
        if numero >=10:
            mayores_a_10.append(numero)
    print(f"Mayores a 10: {mayores_a_10}")