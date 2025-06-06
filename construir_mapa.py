import pygame
from variables import BLANCO, MORADO

class Mapa:
    def __init__(self):
        self.color_pared = MORADO

    def dibujar(self, pantalla):
        pantalla.fill(BLANCO)

        
        pygame.draw.rect(pantalla, self.color_pared, (140, 20, 20, 100))
        pygame.draw.rect(pantalla, self.color_pared, (140, 180, 20, 100))
        
        
        pygame.draw.rect(pantalla, self.color_pared, (60, 140, 180, 20))
