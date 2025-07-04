import pygame
import matriz_mapa

class Tile_1(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/pared_derecha.png")
        self.rect =self.image.get_rect(topleft=pos) #en la esquina superior  izquierda

        self.hitbox =self.rect .inflate(0, -10)
class Tile_2(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/pared_izquierda.png")
        self.rect =self.image.get_rect(topleft=pos)

        self.hitbox =self.rect .inflate(0, -10)

class Tile_3(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/pared_arriba.png")
        self.rect =self.image.get_rect(topleft=pos)

        self.hitbox =self.rect .inflate(0, -10)

class Tile_4(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/pared_abajo.png")
        self.rect =self.image.get_rect(topleft=pos)
        #overlap

        self.hitbox =self.rect .inflate(0, -10)

class Tile_5(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/esquina_1.png")
        self.rect =self.image.get_rect(topleft=pos)

        
class Tile_6(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/esquina_2.png")
        self.rect =self.image.get_rect(topleft=pos)

        

class Tile_7(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/esquina_3.png")
        self.rect =self.image.get_rect(topleft=pos)

        

class Tile_8(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/esquina_4.png")
        self.rect =self.image.get_rect(topleft=pos)

class Tile_9(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/mapa/muro.png")
        self.rect =self.image.get_rect(topleft=pos)
        






