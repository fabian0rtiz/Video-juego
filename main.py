import pygame,sys
from variables import Ancho, Altura, ROJO
from cubo import Jugador
from construir_mapa import Mapa

pygame.init()
pantalla = pygame.display.set_mode((Ancho, Altura))
pygame.display.set_caption("Juego")

jugador = Jugador(60, 60, 40, 40, ROJO)
mapa = Mapa()

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        jugador.manejar_eventos(evento, mapa.paredes)  

    mapa.dibujar(pantalla)
    jugador.dibujar(pantalla)

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

