import pygame
from cubo import Jugador
from variables import ROJO , Ancho , Altura 
class Enemigo(Jugador):
    def _init_(self, x, y, ancho, alto, color):
        super()._init_(x, y, ancho, alto, color)
        self.velocidad = 3  


    def mover_automatico(self, paredes):
       self.x += self.velocidad
       if self.x < 0 or self.x > Ancho :
           self.velocidad *= -1 
          
    def dibujar_2(self, pantalla):
        pygame.draw.rec(pantalla,ROJO,(self.x, self.y, self.ancho, self.alto))
