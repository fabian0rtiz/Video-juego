import pygame
import matriz_mapa
from tiles_mapa import Tile
from jugador import Jugador

class Nivel:
    def __init__(self):
        self.screen= pygame.display.get_surface()
        self.Sprites_deFondo= YGrupoCmara()
        self.Obstaculos = pygame.sprite.Group()

        self.crearMapa()
        

    def crearMapa(self):
        for row_index,row in enumerate(matriz_mapa.mapa):
            for col_index,col in enumerate(row):
                x=col_index*104
                y=row_index*104
                if col=="x":
                    Tile((x,y),[self.Sprites_deFondo,self.Obstaculos])
                if col=="L":
                    self.jugador=Jugador((x,y),[self.Sprites_deFondo],self.Obstaculos)

    
    def corre(self):
        self.Sprites_deFondo.dibuja(self.jugador)
        self.Sprites_deFondo.update()
    
class YGrupoCmara(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen= pygame.display.get_surface()
        self.half_width= self.screen.get_size()[0]//2# estamos pidiendo el tamaño de la ventana pero con el [0], le pedimos el tamaño del eje x
        self.half_height= self.screen.get_size()[1]//2# estamos pidiendo el tamaño de la ventana pero con el [1], le pedimos el tamaño del eje y
        self.offset = pygame.math.Vector2()#indica la posicion inicial en ejes x y dos dimensiones cuando esta vacio va a estar en el centro del jugador 0,0

    def dibuja(self,jugador):
        self.offset.x=jugador.rect.centerx- self.half_width#con esto centramos en el eje x el vector en el personaje
        self.offset.y=jugador.rect.centery- self.half_height#con esto centramos en el eje y el vector en el personaje

        for sprite in sorted(self.sprites(),key=lambda sprite:sprite.rect.centery):#accedemos a todos lo sprites del grupo , lambda es una funciono anonima, se usa para el codigo innesario 
            offset_rect=sprite.rect.topleft - self.offset#esto sera in rectangulo invisible donde se usara para el movimiento de la camara
            self.screen.blit(sprite.image, offset_rect)#la primera dibuja , la segunda indica las posiciones
    
    



