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
        self.offset.x = jugador.rect.centerx - self.half_width
        self.offset.y = jugador.rect.centery - self.half_height

        lista_sprites = list(self.sprites())

        for i in range(len(lista_sprites)):
            for j in range(i + 1, len(lista_sprites)):
                if lista_sprites[i].rect.centery > lista_sprites[j].rect.centery:
                    lista_sprites[i], lista_sprites[j] = lista_sprites[j], lista_sprites[i]
        
        for sprite in lista_sprites:
            pos_en_pantalla = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, pos_en_pantalla)





        
    



