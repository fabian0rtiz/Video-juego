import sys
import pygame  
from cargar_mapa import Nivel 
from tiempo import Tiempo

class Zelda:
    def __init__(self):
        pygame.font.init()
        pygame.init()

        self.screen = pygame.display.set_mode((1100, 550))
        pygame.display.set_caption("calaboso")  
        self.nivel=Nivel()
        self.cronometro = Tiempo(30)
        self.reloj = pygame.time.Clock()

        self.tiempo_ganador = None
        self.tiempo_perdedor = None

    def corre_juego(self): 
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    sys.exit()
               
            self.screen.fill("black")
            self.nivel.corre()
            self.cronometro.actualizar()
            self.cronometro.dibujar(self.screen)

            if self.nivel.ganaste:
                if self.tiempo_ganador is None:
                    self.tiempo_ganador = pygame.time.get_ticks()  # guardar el momento cuando ganaste

                fuente = pygame.font.Font(None, 80)
                texto = fuente.render("¡Has ganado!", True, "white")
                rect_texto = texto.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
                self.screen.blit(texto, rect_texto)

                # después de 3 segundos (3000 ms), salir del juego
                if pygame.time.get_ticks() - self.tiempo_ganador > 3000:
                    sys.exit()

            elif self.cronometro.agotado():
                if self.tiempo_perdedor is None:
                    self.tiempo_perdedor = pygame.time.get_ticks()
                
                fuente = pygame.font.Font(None, 80)
                texto = fuente.render("¡Tiempo agotado!", True, "red")
                rect = texto.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
                self.screen.blit(texto, rect)

                if pygame.time.get_ticks() - self.tiempo_perdedor > 3000:
                  sys.exit()


            pygame.display.update()
            self.reloj.tick(60)  

            

if __name__ == "__main__":
    zelda_juego = Zelda()
    zelda_juego.corre_juego()
