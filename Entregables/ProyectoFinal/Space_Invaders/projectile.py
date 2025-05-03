import pygame

# Clase para los proyectiles
class Projectile:
    def __init__(self, x, y, speed, image):
        self.image = image
        self.rect = pygame.Rect(x, y, 5, 10)  # Tamaño del proyectil
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
