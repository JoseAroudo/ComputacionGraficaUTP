import pygame
import random
from projectile import Projectile

class Enemy:
    def __init__(self, x, y, speed, life, bullet_speed, image, laser_image):
        self.image = pygame.transform.scale(image, (40, 30))  # Escalar la imagen a 40x30
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.life = life
        self.bullet_speed = bullet_speed
        self.laser_image = laser_image
        self.lasers = []

    def move(self):
        self.rect.x += self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:  # Limitar ancho de pantalla
            self.speed *= -1

    def shoot(self):
        if random.randint(0, 100) < 5:  # Probabilidad de disparo
            laser = Projectile(self.rect.centerx, self.rect.bottom, self.bullet_speed, self.laser_image)
            self.lasers.append(laser)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for laser in self.lasers:
            laser.draw(surface)

    def update(self, screen_height):
        self.move()
        self.shoot()
        for laser in self.lasers:
            laser.move()
            if laser.rect.top > screen_height:
                self.lasers.remove(laser)

    def take_damage(self):
        self.life -= 1
        return self.life <= 0  # Devuelve True si está destruido
