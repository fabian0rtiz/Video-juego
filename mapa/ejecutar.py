import sys
import pygame
from cargar_mapa import Mapa

class Zelda:
    def __init__(self):
        pygame.init()
        self.scream=pygame.display.set_mode((1100,550))
        pygame.display.set_caption("Laberinto")
        self.nivel=Mapa()

    def correr_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.scream.fill("black")
            self.nivel.ejecutar_mapa()
            pygame.display.update()

if __name__=="__main__":
    laberinto_juego=Zelda()
    laberinto_juego.correr_juego()