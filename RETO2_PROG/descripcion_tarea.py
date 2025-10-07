# Se integrará una lista con las constantes y un diccionario con datos importantes de la simulación

# Rendimiento de aeronave en diferentes condiciones
rendimiento_simulación = {
    "información de cohete": {
        "Altura": 43,  # metros
        "Diámetro": 7,  # metros
        "Fairing": 5,  # metros
    },
    "Altitud": {  # 200 km
        "velocidad_despegue1": 5, # km/min
        "velocidad_despegue2": 3, # km/min
        "Consumo_comb1": 800, #km/min
        "Consumo_comb2": 500, #km/min
    }
}



simulacion = ["objetivo altitud", "consumo etapa 1", "consumo etapa 2", "Incremento A1", "Imcremento A2"]

def sim_cohete(combustible_e1, combustible_e2):
    objetivo_alt = 200
    consumo_1 = 800
    consumo_2 = 500
    IA1 = 5
    IA2 = 3

    altitud = 0
    minuto = 0
    etapa = 1

    while altitud < objetivo_alt:
        print(simulacion[0])
        if etapa == 1:
            if combustible_e1 > 0:
                combustible_e1 -= consumo_1
                print(simulacion[1])
                altitud += IA1
                print(simulacion[3])
                minuto += 1
            else:
                etapa = 2
        elif etapa == 2:
            if combustible_e2 > 0:
                combustible_e2 -= consumo_2
                print(simulacion[2])
                altitud += IA2
                print(simulacion[4])
                minuto += 1
            else:
                print("\nEl cohete se quedó sin combustible en la etapa 2.")
                print("Altitud alcanzada:", altitud, "km")
                return

    print("\nEl cohete alcanzó la órbita de 200 km en", minuto, "minutos.")

while True:
    print("\n--- Simulación de lanzamiento de cohete ---")
    combustible_e1 = int(input("Ingrese la cantidad de combustible de la etapa 1 (kg): "))
    combustible_e2 = int(input("Ingrese la cantidad de combustible de la etapa 2 (kg): "))

    sim_cohete(combustible_e1, combustible_e2)

    continuar = input("\n¿Desea realizar otra simulación? (SI/NO): ").upper()
    if continuar == "NO":
        print("Simulación finalizada.")
        break
