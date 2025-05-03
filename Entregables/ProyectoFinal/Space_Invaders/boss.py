import pygame
import random
from projectile import Projectile

class Boss:
    def __init__(self, x, y, speed, life, bullet_speed, image, screen_width, laser_image):
        self.image = pygame.transform.scale(image, (100, 60))  # Tamaño más grande para el jefe
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.life = life
        self.bullet_speed = bullet_speed
        self.laser_image = laser_image
        self.lasers = []
        self.screen_width = screen_width

    def move(self):
        """Movimiento horizontal como los enemigos."""
        self.rect.x += self.speed
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            self.speed *= -1

    def shoot(self):
        """Dispara dos proyectiles: uno desde cada cañón."""
        if random.randint(0, 100) < 20:  # Probabilidad más alta para disparar
            left_cannon = self.rect.left + 10  # Posición del cañón izquierdo
            right_cannon = self.rect.right - 10  # Posición del cañón derecho
            laser_left = Projectile(left_cannon, self.rect.bottom, self.bullet_speed, self.laser_image)
            laser_right = Projectile(right_cannon, self.rect.bottom, self.bullet_speed, self.laser_image)
            self.lasers.extend([laser_left, laser_right])

    def draw(self, surface):
        """Dibuja al jefe y sus proyectiles."""
        surface.blit(self.image, self.rect)
        for laser in self.lasers:
            laser.draw(surface)

    def update(self, screen_height):
        """Actualiza la posición y los disparos."""
        self.move()
        self.shoot()
        for laser in self.lasers:
            laser.move()
            if laser.rect.top > screen_height:
                self.lasers.remove(laser)

    def take_damage(self):
        """Reduce la vida del jefe al recibir disparos."""
        self.life -= 1
        return self.life <= 0  # Devuelve True si el jefe es derrotado
