import pygame
from projectile import Projectile

# Configuración del jugador
PLAYER_SPEED = 5
BULLET_SPEED = -10

class Player:
    def __init__(self, image, start_pos, screen_width, laser_image):
        self.image = pygame.transform.scale(image, (50, 40))
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = PLAYER_SPEED
        self.lasers = []
        self.screen_width = screen_width
        self.laser_image = laser_image

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < self.screen_width:
            self.rect.x += self.speed

    def shoot(self, laser_sound, laser_image):
        laser = Projectile(self.rect.centerx, self.rect.top, BULLET_SPEED, laser_image)
        self.lasers.append(laser)
        laser_sound.play()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for laser in self.lasers:
            laser.draw(surface)

    def update(self):
        for laser in self.lasers:
            laser.move()
            if laser.rect.bottom < 0:
                self.lasers.remove(laser)