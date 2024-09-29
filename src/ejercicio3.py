from ejercicio1 import calcula_imc
from ejercicio2 import calcula_estado_nutricional

def imprime_estados_nutricionales(tupla):
    
    return(f"Tu IMC es: {calcula_imc(tupla[0],tupla[1])}, {calcula_estado_nutricional(tupla[0],tupla[1])}")

if __name__=="__main__":
    peso=float(input("¿Cuál es su peso?"))
    altura=float(input("¿Cuál es su altura?"))
    print(f"Su IMC es: {calcula_imc(peso,altura)}")
    print(calcula_estado_nutricional(peso,altura))
    datos=[(60.0, 1.6),(75.4, 1.75),(87.9, 1.69),(45.1, 1.65)]
for p in datos:
    input(imprime_estados_nutricionales(p))
    

