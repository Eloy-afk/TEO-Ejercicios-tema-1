from datetime import date
def calcula_dia_semana(fecha):
    dias_semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_semana=fecha.weekday()
    return dias_semana[dia_semana]

if __name__=="__main__":
    dia=int(input("¿Qué día nació usted? "))
    mes=int(input("¿Qué mes nació usted? "))
    año=int(input("¿Qué año nació usted? "))

    fecha_nacimiento=date(año,mes,dia)
    dia_semana=calcula_dia_semana(fecha_nacimiento)
    print(f"Usted nació un: {dia_semana}")