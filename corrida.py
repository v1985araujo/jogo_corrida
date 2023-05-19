from carros import *
from random import uniform
from decimal import Decimal
from datetime import datetime, timedelta
import time

road = []

def iniciar_jogo(start):    
    moment = None
    chegada = 4309      # Distância em metros de uma volta em Interlagos
    venceu = False
    
    road, start = prepara_corrida()
    print("Foi dada a largada!!!!!\n")

    while not venceu:        
        for car in road:
            if car.get_m() >= chegada:
                moment = datetime.now() - start
                #f'Parcial {round(moment.total_seconds(), 4)} por {car.get_brand()} {car.get_model()} na cor {car.get_color()} a {car.get_speed()}km/h'
                #print(f'Desenvolveu em média {round((Decimal(str(car.get_km())) / Decimal(str(moment.total_seconds())) / Decimal("3.6")), 2)} Km/h\n\n')
                venceu = True
                break

            elif car.get_m() < chegada:
                time.sleep(1)       # Causamos uma variação de tempo para calcular a aceleração do carro
                moment = datetime.now() - start                
         
                car.calcula_distancia(Decimal(str(uniform(-.05, 25))), Decimal(str(moment.total_seconds())))

        if (datetime.now() - start) >= timedelta(minutes = 1, seconds = 30):
            break

    return road          

road = iniciar_jogo(datetime.now())

# Definindo a ordem de chegada, com base na distância que cada carro percorreu
road.sort(key = lambda x:x.get_m(), reverse = True)

# Demora aproximadamente 1 minuto para chegar aqui, imaginem que os carros estão acelerando e brecando nas curvas do circuito
print("Ordem de Chegada:")
for position, car in enumerate(road):
    print(f"Em {position + 1}º: {car.get_brand()} {car.get_model()} na cor {car.get_color()} a {round(car.get_speed() * Decimal('3.6'), 2)}km/h, andou {round(car.get_m() / Decimal(1000), 2)}km")