import pygame
import matriz_mapa
from tiles_mapa import Tile
from jugador import Jugador
from meta import Meta

class Nivel:
    def __init__(self):
        self.screen= pygame.display.get_surface()
        self.Sprites_deFondo= YGrupoCmara()
        self.Obstaculos = pygame.sprite.Group()
        self.Metas = pygame.sprite.Group()
        self.ganaste=False


        self.crearMapa()
        

    def crearMapa(self):
        for row_index,row in enumerate(matriz_mapa.mapa):
            for col_index,col in enumerate(row):
                x=col_index*104
                y=row_index*104
                if col=="x":
                    Tile((x,y),[self.Sprites_deFondo,self.Obstaculos])

                if col=="M":
                    Meta((x,y),[self.Sprites_deFondo,self.Metas])
        
                if col=="L":
                    self.jugador=Jugador((x,y),[self.Sprites_deFondo],self.Obstaculos)

    
    def corre(self):
        self.Sprites_deFondo.dibuja(self.jugador)
        self.Sprites_deFondo.update()

        if not self.ganaste and pygame.sprite.spritecollideany(self.jugador, self.Metas):
          self.ganaste = True
        if self.ganaste:
         fuente = pygame.font.Font(None, 80)
         texto = fuente.render("¡Has ganado!", True, "white")
         rect_texto = texto.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
         self.screen.blit(texto, rect_texto)
         
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
            for j in range(i + 1, len(lista_sprites)):#el i +1 es para q no se compare consigo mismo sino se quedaria estatico
                if lista_sprites[i].rect.centery > lista_sprites[j].rect.centery: #este condicional nos ayuda a comparar las posiciones de nuestra lista de sprites donde al momento de tener que recorrer una mas arriba hay q actualizar la posicion central con la dubla
                    lista_sprites[i], lista_sprites[j] = lista_sprites[j], lista_sprites[i]
        
        for sprite in lista_sprites:
            pos_en_pantalla = sprite.rect.topleft - self.offset #lo restamos con la posicion real y con el cuadro del vector para tener la perspectiva
            self.screen.blit(sprite.image, pos_en_pantalla)#esto dibuja el sprite y la posicion ajustada
  



