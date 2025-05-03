import pygame
import sys

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.running = True
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 50)
        self.font_small = pygame.font.Font(None, 36)
        self.width = width
        self.height = height
        self.background = pygame.image.load("Assets/menu.png")

    def show_menu(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))

            # Título del juego
            title = self.font_large.render("Space Invaders", True, (255, 255, 255))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, self.height // 4))

            # Opciones del menú
            play_option = self.font_medium.render("Presiona ENTER para jugar", True, (255, 255, 0))
            instructions_option = self.font_medium.render("Presiona I para instrucciones", True, (255, 255, 0))
            exit_option = self.font_medium.render("Presiona ESC para salir", True, (255, 255, 0))

            self.screen.blit(play_option, (self.width // 2 - play_option.get_width() // 2, self.height // 2))
            self.screen.blit(instructions_option, (self.width // 2 - instructions_option.get_width() // 2, self.height // 2 + 60))
            self.screen.blit(exit_option, (self.width // 2 - exit_option.get_width() // 2, self.height // 2 + 120))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "play"
                    elif event.key == pygame.K_i:
                        self.show_instructions()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()

    def show_instructions(self):
        while True:
            self.screen.fill((0, 0, 0))

            instructions = [
                "Instrucciones del Juego:",
                "1. Usa las flechas izquierda y derecha para mover la nave.",
                "2. Presiona ESPACIO para disparar proyectiles.",
                "3. Destruye los enemigos para avanzar niveles.",
                "4. Evita los disparos enemigos.",
                "5. Derrota al jefe final en el último nivel.",
                "Presiona ESC para regresar al menú principal."
            ]

            for i, line in enumerate(instructions):
                text = self.font_small.render(line, True, (255, 255, 255))
                self.screen.blit(text, (50, 100 + i * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return