import pygame
import matriz_mapa

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstaculos):
        super().__init__(groups)

        self.image =pygame.image.load("image9x3.png")
        self.rect =self.image.get_rect(topleft=pos)
        self.hitbox= self.rect.inflate(0,-20)
        
        self.direccion =pygame.math.Vector2() #vector 2 es para tener eje x y 
        self.velocidad=1

        self.Obstaculos=obstaculos
    
    def teclado(self):
        keys= pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direccion.y=-1 #sube el personaje
        elif keys[pygame.K_DOWN]:
            self.direccion.y=1 #baja el personaje
        
        else:
            self.direccion.y=0
        
        if keys[pygame.K_RIGHT]:
            self.direccion.x=1 
        elif keys[pygame.K_LEFT]:
            self.direccion.x=-1 
        
        else:
            self.direccion.x=0
    def mover(self,velocidad):
        if self.direccion.magnitude() !=0:
            self.direccion= self.direccion.normalize()
        
        self.hitbox.x += self.direccion.x *velocidad
        self.colisiones("horizontal")

        self.hitbox.y += self.direccion.y *velocidad
        self.colisiones("vertical")
        self.rect.center = self.hitbox.center

    def colisiones(self,direccion):
        if direccion =="horizontal":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direccion.x > 0:
                        self.hitbox.right=sprite.rect.left # esta chocando y lo igualamanos a la pared para q no pase
                    if self.direccion.x < 0:
                        self.hitbox.left =sprite.rect.right
        if direccion =="vertical":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direccion.y > 0:
                        self.hitbox.bottom=sprite.rect.top # esta chocando y lo igualamanos a la pared para q no pase
                    if self.direccion.y < 0:
                        self.hitbox.top =sprite.rect.bottom

    def update(self):
        self.teclado()
        self.mover(self.velocidad)