from decimal import Decimal
from datetime import datetime


class Carro:
    def __init__(self, marca: str, modelo: str, cor: str, motor: str, limite: int):
        """
        Construtor da classe Carro:
        :self: A instância da classe (objeto criado)
        :param marca: marca do carro, retornado com get_brand()
        :param modelo: modelo do carro, retornado com get_model()
        :param cor: cor do carro, retornado com get_color()
        :param motor: motor do carro, retornado com get_engine()
        :param limite: até quantos km/h o carro pode acelerar, retornado com get_limit()
        """      
        self.__brand = marca
        self.__model = modelo
        self.__color = cor
        self.__engine = motor
        self.__limit = limite
        self.__m = 0                # Distânciam percorrida
        self.__speed = 0            # Velocidade do carro (m/s)
        self.__tempo = 0            # Quanto tempo o carro gastou no percurso? (segundos)

    
    def get_brand(self):
        return self.__brand
    
    
    def get_color(self):
        return self.__color
    

    def get_engine(self):
        return self.__engine
    
    
    def get_m(self):
        return self.__m
    
    
    def set_m(self, m):
        raise ValueError("Não se deve adulterar o odômetro!!! use o método calcula_distancia() e forneça a velocidade e o timedelta.total_seconds()")
        

    def get_limit(self):
        return self.__limit
    
    
    def set_limit(self, limit):
        raise ValueError("Opção inválida: não se altera a velocidade máxima do carro")
    
    
    def get_model(self):
        return self.__model    
    
    
    def get_speed(self):        
        return self.__speed
    
    
    def get_tempo(self):
        return self.__tempo
        

    def calcula_distancia(self, speed, tempo):
        self.__acelerar(speed, tempo)
        #self.__tempo += abs(tempo)        
        #self.__percorrer_distancia(abs(Decimal(self.__speed) * Decimal(self.__tempo)))

    
    def __percorrer_distancia(self, distancia):
        self.__m += abs(distancia)
    
    
    def __acelerar(self, velocidade, tempo):
        """
        método que aumenta a velocidade do carro quando recebe um número positivo, desde que dentro do limite que pode acelerar

        :self: A instância da classe
        :param velocidade:   o número que vai alterar a velocidade do carro. Se o número for negativo, vai frear o carro (é calculado em m/s)
        :param tempo:        é esperado que seja o timedelta.total_seconds()
        """
        
        velocidade = Decimal(velocidade)
            
        deltaT = abs(Decimal(tempo) - Decimal(self.__tempo))
        self.__tempo += tempo
            
        deltaV = velocidade - Decimal(self.__speed)

        acelera = deltaV / deltaT       #calculado em m/s²
        
            #if self.__speed + (acelera * tempo) <= self.__limit:

        if self.__speed + (acelera * tempo) <= (Decimal(self.__limit) / Decimal('3.6')) and self.__speed + (acelera * tempo) > 0:   # velocidade em m/s, limite em km/h
            
            self.__speed = self.__speed + (acelera * tempo)
        
        self.__percorrer_distancia(abs(self.__speed * tempo))      #odômetro calculado em metros

        #if self.__speed + x <= self.__limit:
        #    if self.__speed + x >= 0:
        #        self.__speed += x
        #    else: 
        #        self.__speed = 50
        #else: 
        #    self.__speed = self.__limit        
       
                    
    def parar(self):
        """
        método que para o carro imediatamente, não recebe parâmetros além da própria instância
        :self: A instância da classe
        """
        self.__speed = 0


#Herança (super() refere-se à mãe declarada na classe filha, passando acesso aos métodos já que cada instância é "linkada")
class AM(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Aston Martin", modelo, cor, motor, limite)

class Ferrari(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Ferrari", modelo, cor, motor, limite)

class Lamborghini(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Lamborghini", modelo, cor, motor, limite)

class Mercedes(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Mercedes-Benz", modelo, cor, motor, limite)       

class Nissan(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Nissan", modelo, cor, motor, limite)

class Porsche(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Porsche", modelo, cor, motor, limite)

class VW(Carro):
    def __init__(self, modelo, cor, motor, limite):
        super().__init__("Volkswagen", modelo, cor, motor, limite)


def prepara_corrida():
    f40 = Ferrari("F40", "vermelha", "2.9L V8 Bi-Turbo", 324)              #RWD (bi turbo são 2 turbinas diferentes)
    f50 = Ferrari("F50", "laranja", "4.7L V12", 325)                       #RWD (https://autopapo.uol.com.br/curta/ferrari-f50-tranco/)
    gal = Lamborghini("Gallardo", "azul", "5.0L V10", 318)                 #AWD (viatura italiana)
    mur = Lamborghini("Murciélago", "grafite", "6.5L V12", 340)            #RWD 
    p959 = Porsche("959", "preta", "2.8L Boxer 6 Bi-Turbo", 339)           #AWD 
    p911 = Porsche("911", "amarela", "4.0L Boxer 6 Turbo", 330)            #RWD
    cl6 = Mercedes("CL65 AMG", "prata", "6.0L V12 Turbo", 340)             #RWD
    v12 = AM("V12 Vantage", "prata", "5.2L V12 Twin Turbo", 322)           #RWD (twin turbo são 2 turbinas iguais)

    return [cl6, f40, f50, gal, mur, p911, p959, v12], datetime.now()
    #return [p959, f40], datetime.datetime.now() #teste simplificado, que historicamente o Porsche 959 ganha da Ferrari F40