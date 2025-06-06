import time
class Tiempo: 
    def __init__(self, tiempo_limite, tiempo_acutal=None):
        self.tiempo_limite = tiempo_limite
        self.tiempo_actual = tiempo_acutal

    def iniciar_cuenta_regresiva(self):
        for self.tiempo_actual in range (self.tiempo_limite, -1, -1): #se usa -1 para que imprima hasta 0
            self.verificar_tiempo()
            time.sleep(1)

    def verificar_tiempo(self):
        print(self.tiempo_actual)

    def tiempo_agotado(self):
        if (self.tiempo_actual == 0):
            print("se agotó el tiempo")

cronómetro_01 = Tiempo(5)
cronómetro_01.iniciar_cuenta_regresiva()
cronómetro_01.tiempo_agotado()

