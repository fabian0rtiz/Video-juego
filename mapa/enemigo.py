import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos):
        super().__init__(groups)

        self.image = pygame.image.load("imagenes/enemigo.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-40, -40)

        self.direccion = pygame.math.Vector2(1, 0)  # Comienza moviéndose a la derecha
        self.velocidad = 2
        self.obstaculos = obstaculos

    def mover(self):
        self.hitbox.x += self.direccion.x * self.velocidad

        for obstaculo in self.obstaculos:
            if obstaculo.rect.colliderect(self.hitbox):
                # Rebota: invierte la dirección al chocar
                self.direccion.x *= -1
                self.hitbox.x += self.direccion.x * self.velocidad
                break  # Solo necesita rebotar una vez por frame

        # Actualiza rect para dibujar
        self.rect.center = self.hitbox.center

    def update(self):
        self.mover()

<<<<<<< HEAD



=======
        # Colisión con jugador
        if self.jugador.rect.colliderect(self.rect):
            self.jugador.morir()  
>>>>>>> 450e04866abdb37c1dde1cd752562153676ca3aa
