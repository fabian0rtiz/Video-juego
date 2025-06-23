import pygame
import time

class Tiempo:
    def __init__(self, tiempo_limite):
        self.tiempo_limite = tiempo_limite #el tiempo total
        self.tiempo_actual = tiempo_limite #el tiempo q ira disminuyendo
        self.ultimo_tiempo = time.time() #nos da la hora actual , se usara para hacer las comparaciones
        self.font = pygame.font.Font(None, 36)#fuennte de texto(tipo de texto,tamaño)

    def actualizar(self):
        tiempo_actual = time.time()
        if tiempo_actual - self.ultimo_tiempo >= 1:
            self.tiempo_actual -= 1
            self.ultimo_tiempo = tiempo_actual

    def dibujar(self, pantalla):
        texto = f"Tiempo: {self.tiempo_actual}"
        superficie = self.font.render(texto, True, (255, 255, 255))
        pantalla.blit(superficie, (10, 10))

    def agotado(self):
        return self.tiempo_actual <= 0
