import pygame
import matriz_mapa
from tiles_mapa import Tile

class Mapa:
    def __init__(self):
        self.scream=pygame.display.get_surface()
        self.sprite_fondo=pygame.sprite.Group()
        self.obstaculo=pygame.sprite.Group()

        self.crearMapa()

    def crearMapa(self):
        for row_index,row in enumerate(matriz_mapa.mapa2):
            for col_index,col in enumerate(row):
                x=col_index*30
                y=row_index*30
                if col==1:
                    Tile((x,y),[self.sprite_fondo,self.obstaculo])

    def ejecutar_mapa(self):
        self.sprite_fondo.draw(self.scream)


