def calcula_imc(peso,altura):
    IMC=peso/(altura**2)
    return round(IMC,2)

if __name__=="__main__":
    peso=float(input("¿Cuál es su peso?"))
    altura=float(input("¿Cuál es su altura?"))
    print(f"Su IMC es: {calcula_imc(peso,altura)}")


