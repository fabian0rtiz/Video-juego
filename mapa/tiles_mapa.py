import pygame
import matriz_mapa

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image=pygame.image.load("tite (4).png")
        self.rect=self.image.get_rect(topleft=pos)
