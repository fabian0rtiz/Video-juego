import pygame
import matriz_mapa

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image =pygame.image.load("imagenes/pared_2.png")
        self.rect =self.image.get_rect(topleft=pos)
#overlap
        self.hitbox =self.rect .inflate(0, -10)#el inflate cambia el tamaño del rectangulo , lo minimiza (x,y), en el eje y estamos restando 5 arriba y 5 abajo
