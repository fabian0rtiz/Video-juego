import sys
import pygame  
from cargar_mapa import Nivel 
from tiempo import Tiempo

class Zelda:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 550))
        pygame.display.set_caption("calaboso")  
        self.nivel=Nivel()
        self.cronometro = Tiempo(60)
        self.reloj = pygame.time.Clock()

    def corre_juego(self): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    sys.exit()
               
            self.screen.fill("black")
            self.nivel.corre()
            self.cronometro.actualizar()
            self.cronometro.dibujar(self.screen)

            if self.cronometro.agotado():
                print("¡Tiempo agotado!")
                sys.exit()
            pygame.display.update()
            self.reloj.tick(60)  

            

if __name__ == "__main__":
    zelda_juego = Zelda()
    zelda_juego.corre_juego()
