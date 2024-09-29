from ejercicio1 import calcula_imc

def calcula_estado_nutricional(peso,altura):
    IMC=calcula_imc(peso,altura)
    if IMC<18.5:
        input("Tienes un peso muy bajo.")
    elif 18.5<IMC<25:
        input("Tienes un peso normal.")
    elif 25<IMC<30:
        input("Tienes sobrepeso.")
    else:
        input("Tienes obesidad.")



if __name__=="__main__":
    peso=float(input("¿Cuál es su peso?"))
    altura=float(input("¿Cuál es su altura?"))
    print(f"Su IMC es: {calcula_imc(peso,altura)}")
    print(calcula_estado_nutricional(peso,altura))
